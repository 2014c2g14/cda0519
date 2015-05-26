# coding=utf-8
# 上面的程式內容編碼必須在程式的第一或者第二行才會有作用

################# (1) 模組導入區
# 導入 cherrypy 模組, 為了在 OpenShift 平台上使用 cherrypy 模組, 必須透過 setup.py 安裝



import cherrypy
# 導入 Python 內建的 os 模組, 因為 os 模組為 Python 內建, 所以無需透過 setup.py 安裝
import os
# 導入 random 模組
import random
import math
from cherrypy.lib.static import serve_file
# 導入 gear 模組
#import gear
import man
import man2

################# (2) 廣域變數設定區
# 確定程式檔案所在目錄, 在 Windows 下有最後的反斜線
_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
# 設定在雲端與近端的資料儲存目錄
if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示程式在雲端執行
    download_root_dir = os.environ['OPENSHIFT_DATA_DIR']
    data_dir = os.environ['OPENSHIFT_DATA_DIR']
else:
    # 表示程式在近端執行
    download_root_dir = _curdir + "/local_data/"
    data_dir = _curdir + "/local_data/"



import cherrypy

# 這是 MAN 類別的定義
'''
# 在 application 中導入子模組
import programs.cdag3.man as cdag3_man
# 加入 cdag3 模組下的 man.py 且以子模組 man 對應其 MAN() 類別
root.cdag3.man = cdag3_man.MAN()

# 完成設定後, 可以利用
/cdag3/man/assembly
# 呼叫 man.py 中 MAN 類別的 assembly 方法
'''
class MAN(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014CDA 協同專案下的 cdag30 模組下的 MAN 類別.<br /><br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<a href="assembly">執行  MAN 類別中的 assembly 方法</a><br /><br />
請確定下列零件於 V:/home/lego/man 目錄中, 且開啟空白 Creo 組立檔案.<br />
<a href="/static/lego_man.7z">lego_man.7z</a>(滑鼠右鍵存成 .7z 檔案)<br />
'''
        return outstring

    @cherrypy.expose
    def assembly(self, *args, **kwargs):
        outstring = '''
<!DOCTYPE html> 
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<script type="text/javascript" 
src="/static/weblink/examples/jscript/pfcUtils.js"></script>

<script type="text/javascript"
src="/static/weblink/examples/jscript/wl_headers.js"></script>
</head>
<body>
</script><script language="JavaScript">

/*設計一個零件組立函式*/
// featID 為組立件第一個組立零件的編號
// inc 則為 part1 的組立順序編號, 第一個入組立檔編號為 featID+0
// part2 為外加的零件名稱
function axis_plane_assembly(session, assembly, transf, featID, inc, part2, axis1, plane1, axis2, plane2){
var descr = pfcCreate("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/"+part2);
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
    var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
var ids = pfcCreate("intseq");
ids.Append(featID+inc);
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
var asmDatums = new Array(axis1, plane1);
var compDatums = new Array(axis2, plane2);
var relation = new Array (pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN, pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
var relationItem = new Array(pfcCreate("pfcModelItemType").ITEM_AXIS, pfcCreate("pfcModelItemType").ITEM_SURFACE);
var constrs = pfcCreate("pfcComponentConstraints");
    for (var i = 0; i < 2; i++)
    {
        var asmItem = subassembly.GetItemByName (relationItem[i], asmDatums [i]);
        if (asmItem == void null)
        {
            interactFlag = true;
            continue;
        }
        var compItem = componentModel.GetItemByName (relationItem[i], compDatums [i]);
        if (compItem == void null)
        {
            interactFlag = true;
            continue;
        }
        var MpfcSelect = pfcCreate ("MpfcSelect");
        var asmSel = MpfcSelect.CreateModelItemSelection (asmItem, subPath);
        var compSel = MpfcSelect.CreateModelItemSelection (compItem, void null);
        var constr = pfcCreate("pfcComponentConstraint").Create (relation[i]);
        constr.AssemblyReference  = asmSel;
        constr.ComponentReference = compSel;
        constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (true, false);
        constrs.Append(constr);
    }
asmcomp.SetConstraints(constrs, void null);
}
// 以上為 axis_plane_assembly() 函式
//
function three_plane_assembly(session, assembly, transf, featID, inc, part2, plane1, plane2, plane3, plane4, plane5, plane6){
var descr = pfcCreate("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/"+part2);
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
    var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
var ids = pfcCreate("intseq");
ids.Append(featID+inc);
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
var constrs = pfcCreate("pfcComponentConstraints");
var asmDatums = new Array(plane1, plane2, plane3);
var compDatums = new Array(plane4, plane5, plane6);
var MpfcSelect = pfcCreate("MpfcSelect");
for (var i = 0; i < 3; i++)
{
    var asmItem = subassembly.GetItemByName(pfcCreate("pfcModelItemType").ITEM_SURFACE, asmDatums[i]);
    
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
    var compItem = componentModel.GetItemByName(pfcCreate("pfcModelItemType").ITEM_SURFACE, compDatums[i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
    var asmSel = MpfcSelect.CreateModelItemSelection(asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection(compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create(pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
    constr.AssemblyReference = asmSel;
    constr.ComponentReference = compSel;
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (false, false);
    constrs.Append(constr);
}
asmcomp.SetConstraints(constrs, void null);
}
// 以上為 three_plane_assembly() 函式
//
// 假如 Creo 所在的操作系統不是 Windows 環境
if (!pfcIsWindows())
// 則啟動對應的 UniversalXPConnect 執行權限 (等同 Windows 下的 ActiveX)
netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
// pfcGetProESession() 是位於 pfcUtils.js 中的函式, 確定此 JavaScript 是在嵌入式瀏覽器中執行
var session = pfcGetProESession();
// 設定 config option, 不要使用元件組立流程中內建的假設約束條件
session.SetConfigOption("comp_placement_assumptions","no");
// 建立擺放零件的位置矩陣, Pro/Web.Link 中的變數無法直接建立, 必須透過 pfcCreate() 建立
var identityMatrix = pfcCreate("pfcMatrix3D");
// 建立 identity 位置矩陣
for (var x = 0; x < 4; x++)
for (var y = 0; y < 4; y++)
{
    if (x == y)
        identityMatrix.Set(x, y, 1.0);
    else
        identityMatrix.Set(x, y, 0.0);
}
// 利用 identityMatrix 建立 transf 座標轉換矩陣
var transf = pfcCreate("pfcTransform3D").Create(identityMatrix);
// 取得目前的工作目錄
var currentDir = session.getCurrentDirectory();
// 以目前已開檔的空白組立檔案, 作為 model
var model = session.CurrentModel;
// 查驗有無 model, 或 model 類別是否為組立件, 若不符合條件則丟出錯誤訊息
if (model == void null || model.Type != pfcCreate("pfcModelType").MDL_ASSEMBLY)
throw new Error (0, "Current model is not an assembly.");
// 將此模型設為組立物件
var assembly = model;

/**---------------------- LEGO_BODY--------------------**/
// 設定零件的 descriptor 物件變數
var descr = pfcCreate("pfcModelDescriptor").CreateFromFileName("v:/home/lego/man/LEGO_BODY.prt");
// 若零件在 session 則直接取用
var componentModel = session.GetModelFromDescr(descr);
// 若零件不在 session 則從工作目錄中載入 session
var componentModel = session.RetrieveModel(descr);
// 若零件已經在 session 中則放入組立檔中
if (componentModel != void null)
{
    // 注意這個 asmcomp 即為設定約束條件的本體
    // asmcomp 為特徵物件, 直接將零件, 以 transf 座標轉換矩陣方位放入組立檔案中
    var asmcomp = assembly.AssembleComponent(componentModel, transf);
}

// 建立約束條件變數
var constrs = pfcCreate("pfcComponentConstraints");
// 設定組立檔中的三個定位面, 注意內定名稱與 Pro/E WF 中的 ASM_D_FRONT 不同, 而是 ASM_FRONT, 可在組立件->info->model 中查詢定位面名稱
// 組立檔案中的 Datum 名稱也可以利用 View->plane tag display 查詢名稱
// 建立組立參考面所組成的陣列
var asmDatums = new Array("ASM_FRONT", "ASM_TOP", "ASM_RIGHT");
// 設定零件檔中的三個定位面, 名稱與 Pro/E WF 中相同
var compDatums = new Array("FRONT", "TOP", "RIGHT");
// 建立 ids 變數, intseq 為 sequence of integers 為資料類別, 使用者可以經由整數索引擷取此資料類別的元件, 第一個索引為 0
       // intseq 等同 Python 的數列資料?
var ids = pfcCreate("intseq");
// 利用 assembly 物件模型, 建立路徑變數
var path = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
// 採用互動式設定相關的變數, MpfcSelect 為 Module level class 中的一種
var MpfcSelect = pfcCreate("MpfcSelect");
// 利用迴圈分別約束組立與零件檔中的三個定位平面
for (var i = 0; i < 3; i++)
{
// 設定組立參考面, 也就是 "ASM_FRONT", "ASM_TOP", "ASM_RIGHT" 等三個 datum planes
var asmItem = assembly.GetItemByName (pfcCreate("pfcModelItemType").ITEM_SURFACE, asmDatums[i]);
// 若無對應的組立參考面, 則啟用互動式平面選擇表單 flag
if (asmItem == void null)
{
    interactFlag = true;
    continue;
}
// 設定零件參考面, 也就是 "FRONT", "TOP", "RIGHT" 等三個 datum planes
var compItem = componentModel.GetItemByName (pfcCreate ("pfcModelItemType").ITEM_SURFACE, compDatums[i]);
// 若無對應的零件參考面, 則啟用互動式平面選擇表單 flag
if (compItem == void null)
{
    interactFlag = true;
    continue;
}
        // 因為 asmItem 為組立件中的定位特徵, 必須透過 path 才能取得
var asmSel = MpfcSelect.CreateModelItemSelection(asmItem, path);
        // 而 compItem 則為零件, 沒有 path 路徑, 因此第二變數為 null
var compSel = MpfcSelect.CreateModelItemSelection(compItem, void null);
        // 利用 ASM_CONSTRAINT_ALIGN 對齊組立約束建立約束變數
var constr = pfcCreate("pfcComponentConstraint").Create (pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN);
        // 設定約束條件的組立參考與元件參考選擇
constr.AssemblyReference = asmSel;
constr.ComponentReference = compSel;
       // 第一個變數為強制變數, 第二個為忽略變數
       // 強制變數為 false, 表示不強制約束, 只有透過點與線對齊時需設為 true
       // 忽略變數為 false, 約束條件在更新模型時是否忽略, 設為 false 表示不忽略
       // 通常在組立 closed chain 機構時,  忽略變數必須設為 true, 才能完成約束
       // 因為三個面絕對約束, 因此輸入變數為 false, false
constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (false, false);
// 將互動選擇相關資料, 附加在程式約束變數之後
constrs.Append(constr);
}

// 設定組立約束條件
asmcomp.SetConstraints (constrs, void null);
/**---------------------- LEGO_ARM_RT 右手上臂--------------------**/
var descr = pfcCreate ("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/LEGO_ARM_RT.prt");
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
        // 注意這個 asmcomp 即為設定約束條件的本體
        // asmcomp 為特徵物件,直接將零件, 以 transf 座標轉換放入組立檔案中
var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
// 取得 assembly 項下的元件 id, 因為只有一個零件, 採用 index 0 取出其 featID
var components = assembly.ListFeaturesByType(true, pfcCreate ("pfcFeatureType").FEATTYPE_COMPONENT);
// 此一 featID 為組立件中的第一個零件編號, 也就是樂高人偶的 body
var featID = components.Item(0).Id;

ids.Append(featID);
// 在 assembly 模型中建立子零件所對應的路徑
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
// 以下針對 body 的 A_13 軸與 DTM1 基準面及右臂的  A_4 軸線與 DTM1 進行對齊與面接約束
var asmDatums = new Array("A_13", "DTM1");
var compDatums = new Array("A_4", "DTM1");
// 組立的關係變數為對齊與面接
var relation = new Array (pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN, pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
// 組立元件則為軸與平面
var relationItem = new Array(pfcCreate("pfcModelItemType").ITEM_AXIS, pfcCreate("pfcModelItemType").ITEM_SURFACE);
// 建立約束條件變數, 軸採對齊而基準面則以面接進行約束
var constrs = pfcCreate ("pfcComponentConstraints");
for (var i = 0; i < 2; i++)
{
                  // 設定組立參考面, asmItem 為 model item
    var asmItem = subassembly.GetItemByName (relationItem[i], asmDatums [i]);
                  // 若無對應的組立參考面, 則啟用互動式平面選擇表單 flag
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 設定零件參考面, compItem 為 model item
    var compItem = componentModel.GetItemByName (relationItem[i], compDatums[i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 採用互動式設定相關的變數
    var MpfcSelect = pfcCreate ("MpfcSelect");
    var asmSel = MpfcSelect.CreateModelItemSelection (asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection (compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create (relation[i]);
    constr.AssemblyReference  = asmSel;
    constr.ComponentReference = compSel;
                  // 因為透過軸線對齊, 第一 force 變數需設為 true
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (true, false);
                  // 將互動選擇相關資料, 附加在程式約束變數之後
    constrs.Append(constr);
}
// 設定組立約束條件, 以 asmcomp 特徵進行約束條件設定
// 請注意, 第二個變數必須為 void null 表示零件對零件進行約束, 若為 subPath, 則零件會與原始零件的平面進行約束
asmcomp.SetConstraints (constrs, void null);
/**---------------------- LEGO_ARM_LT 左手上臂--------------------**/
var descr = pfcCreate ("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/LEGO_ARM_LT.prt");
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
        // 注意這個 asmcomp 即為設定約束條件的本體
        // asmcomp 為特徵物件,直接將零件, 以 transf 座標轉換放入組立檔案中
var asmcomp = assembly.AssembleComponent(componentModel, transf);
}
// 取得 assembly 項下的元件 id, 因為只有一個零件, 採用 index 0 取出其 featID
var components = assembly.ListFeaturesByType(true, pfcCreate ("pfcFeatureType").FEATTYPE_COMPONENT);
var ids = pfcCreate ("intseq");
// 因為左臂也是與 body 進行約束條件組立,  因此取 body 的 featID
// 至此右臂 id 應該是 featID+1, 而左臂則是 featID+2
ids.Append(featID);
// 在 assembly 模型中建立子零件所對應的路徑
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
var asmDatums = new Array("A_9", "DTM2");
var compDatums = new Array("A_4", "DTM1");
var relation = new Array (pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN, pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
var relationItem = new Array(pfcCreate("pfcModelItemType").ITEM_AXIS, pfcCreate("pfcModelItemType").ITEM_SURFACE);
// 建立約束條件變數
var constrs = pfcCreate ("pfcComponentConstraints");
for (var i = 0; i < 2; i++)
{
                  // 設定組立參考面, asmItem 為 model item
    var asmItem = subassembly.GetItemByName (relationItem[i], asmDatums [i]);
                  // 若無對應的組立參考面, 則啟用互動式平面選擇表單 flag
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 設定零件參考面, compItem 為 model item
    var compItem = componentModel.GetItemByName (relationItem[i], compDatums [i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 採用互動式設定相關的變數
    var MpfcSelect = pfcCreate ("MpfcSelect");
    var asmSel = MpfcSelect.CreateModelItemSelection (asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection (compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create (relation[i]);
    constr.AssemblyReference  = asmSel;
    constr.ComponentReference = compSel;
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (true, false);
                  // 將互動選擇相關資料, 附加在程式約束變數之後
    constrs.Append(constr);
}
// 設定組立約束條件, 以 asmcomp 特徵進行約束條件設定
// 請注意, 第二個變數必須為 void null 表示零件對零件進行約束, 若為 subPath, 則零件會與原始零件的平面進行約束
asmcomp.SetConstraints (constrs, void null);
/**---------------------- LEGO_HAND 右手手腕--------------------**/
// 右手臂 LEGO_ARM_RT.prt 基準  A_2, DTM2
// 右手腕 LEGO_HAND.prt 基準 A_1, DTM3
var descr = pfcCreate ("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/LEGO_HAND.prt");
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
        // 注意這個 asmcomp 即為設定約束條件的本體
        // asmcomp 為特徵物件,直接將零件, 以 transf 座標轉換放入組立檔案中
var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
// 取得 assembly 項下的元件 id, 因為只有一個零件, 採用 index 0 取出其 featID
var components = assembly.ListFeaturesByType(true, pfcCreate ("pfcFeatureType").FEATTYPE_COMPONENT);
var ids = pfcCreate ("intseq");

// 組立件中 LEGO_BODY.prt 編號為 featID
// LEGO_ARM_RT.prt 則是組立件第二個置入的零件,  編號為 featID+1
ids.Append(featID+1);
// 在 assembly 模型中, 根據子零件的編號, 建立子零件所對應的路徑
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
// 以下針對 LEGO_ARM_RT 的 A_2 軸與 DTM2 基準面及 HAND 的  A_1 軸線與 DTM3 進行對齊與面接約束
var asmDatums = new Array("A_2", "DTM2");
var compDatums = new Array("A_1", "DTM3");
// 組立的關係變數為對齊與面接
var relation = new Array (pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN, pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
// 組立元件則為軸與平面
var relationItem = new Array(pfcCreate("pfcModelItemType").ITEM_AXIS, pfcCreate("pfcModelItemType").ITEM_SURFACE);
// 建立約束條件變數, 軸採對齊而基準面則以面接進行約束
var constrs = pfcCreate ("pfcComponentConstraints");
for (var i = 0; i < 2; i++)
{
                  // 設定組立參考面, asmItem 為 model item
    var asmItem = subassembly.GetItemByName (relationItem[i], asmDatums [i]);
                  // 若無對應的組立參考面, 則啟用互動式平面選擇表單 flag
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 設定零件參考面, compItem 為 model item
    var compItem = componentModel.GetItemByName (relationItem[i], compDatums [i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 採用互動式設定相關的變數
    var MpfcSelect = pfcCreate("MpfcSelect");
    var asmSel = MpfcSelect.CreateModelItemSelection(asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection (compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create (relation[i]);
    constr.AssemblyReference  = asmSel;
    constr.ComponentReference = compSel;
                  // 因為透過軸線對齊, 第一 force 變數需設為 true
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (true, false);
                  // 將互動選擇相關資料, 附加在程式約束變數之後
    constrs.Append(constr);
}
// 設定組立約束條件, 以 asmcomp 特徵進行約束條件設定
// 請注意, 第二個變數必須為 void null 表示零件對零件進行約束, 若為 subPath, 則零件會與原始零件的平面進行約束
asmcomp.SetConstraints (constrs, void null);
// 利用函式呼叫組立左手 HAND
axis_plane_assembly(session, assembly, transf, featID, 2, 
                              "LEGO_HAND.prt", "A_2", "DTM2", "A_1", "DTM3");
// 利用函式呼叫組立人偶頭部 HEAD
// BODY id 為 featID+0, 以 A_2 及  DTM3 約束
// HEAD 則直接呼叫檔案名稱, 以 A_2, DTM2 約束
axis_plane_assembly(session, assembly, transf, featID, 0, 
                              "LEGO_HEAD.prt", "A_2", "DTM3", "A_2", "DTM2");
// Body 與 WAIST 採三個平面約束組立
// Body 組立面為 DTM4, DTM5, DTM6
// WAIST 組立面為 DTM1, DTM2, DTM3
three_plane_assembly(session, assembly, transf, featID, 0, "LEGO_WAIST.prt", "DTM4", "DTM5", "DTM6", "DTM1", "DTM2", "DTM3"); 
// 右腳
axis_plane_assembly(session, assembly, transf, featID, 6, 
                              "LEGO_LEG_RT.prt", "A_8", "DTM4", "A_10", "DTM1");
// 左腳
axis_plane_assembly(session, assembly, transf, featID, 6, 
                              "LEGO_LEG_LT.prt", "A_8", "DTM5", "A_10", "DTM1");
// 紅帽
axis_plane_assembly(session, assembly, transf, featID, 5, 
                              "LEGO_HAT.prt", "A_2", "TOP", "A_2", "FRONT");
// regenerate 並且 repaint 組立檔案
assembly.Regenerate (void null);
session.GetModelWindow (assembly).Repaint();    
</script>
</body>
</html>
'''
        return outstring

import cherrypy

# 這是 MAN 類別的定義
'''
# 在 application 中導入子模組
import programs.cdag3.man as cdag3_man
# 加入 cdag3 模組下的 man.py 且以子模組 man 對應其 MAN() 類別
root.cdag3.man = cdag3_man.MAN()

# 完成設定後, 可以利用
/cdag3/man/assembly
# 呼叫 man.py 中 MAN 類別的 assembly 方法
'''
class MAN(object):
    # 各組利用 index 引導隨後的程式執行
    @cherrypy.expose
    def index(self, *args, **kwargs):
        outstring = '''
這是 2014CDA 協同專案下的 cdag30 模組下的 MAN 類別.<br /><br />
<!-- 這裡採用相對連結, 而非網址的絕對連結 (這一段為 html 註解) -->
<a href="assembly">執行  MAN 類別中的 assembly 方法</a><br /><br />
請確定下列零件於 V:/home/lego/man 目錄中, 且開啟空白 Creo 組立檔案.<br />
<a href="/static/lego_man.7z">lego_man.7z</a>(滑鼠右鍵存成 .7z 檔案)<br />
'''
        return outstring

    @cherrypy.expose
    def assembly(self, *args, **kwargs):
        outstring = '''
<!DOCTYPE html> 
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<script type="text/javascript" src="/static/weblink/examples/jscript/pfcUtils.js"></script>
</head>
<body>
</script><script language="JavaScript">
/*設計一個零件組立函式*/
// featID 為組立件第一個組立零件的編號
// inc 則為 part1 的組立順序編號, 第一個入組立檔編號為 featID+0
// part2 為外加的零件名稱
function axis_plane_assembly(session, assembly, transf, featID, inc, part2, axis1, plane1, axis2, plane2){
var descr = pfcCreate("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/"+part2);
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
    var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
var ids = pfcCreate("intseq");
ids.Append(featID+inc);
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
var asmDatums = new Array(axis1, plane1);
var compDatums = new Array(axis2, plane2);
var relation = new Array (pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN, pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
var relationItem = new Array(pfcCreate("pfcModelItemType").ITEM_AXIS, pfcCreate("pfcModelItemType").ITEM_SURFACE);
var constrs = pfcCreate("pfcComponentConstraints");
    for (var i = 0; i < 2; i++)
    {
        var asmItem = subassembly.GetItemByName (relationItem[i], asmDatums [i]);
        if (asmItem == void null)
        {
            interactFlag = true;
            continue;
        }
        var compItem = componentModel.GetItemByName (relationItem[i], compDatums [i]);
        if (compItem == void null)
        {
            interactFlag = true;
            continue;
        }
        var MpfcSelect = pfcCreate ("MpfcSelect");
        var asmSel = MpfcSelect.CreateModelItemSelection (asmItem, subPath);
        var compSel = MpfcSelect.CreateModelItemSelection (compItem, void null);
        var constr = pfcCreate("pfcComponentConstraint").Create (relation[i]);
        constr.AssemblyReference  = asmSel;
        constr.ComponentReference = compSel;
        constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (true, false);
        constrs.Append(constr);
    }
asmcomp.SetConstraints(constrs, void null);
}
// 以上為 axis_plane_assembly() 函式
//
function three_plane_assembly(session, assembly, transf, featID, inc, part2, plane1, plane2, plane3, plane4, plane5, plane6){
var descr = pfcCreate("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/"+part2);
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
    var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
var ids = pfcCreate("intseq");
ids.Append(featID+inc);
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
var constrs = pfcCreate("pfcComponentConstraints");
var asmDatums = new Array(plane1, plane2, plane3);
var compDatums = new Array(plane4, plane5, plane6);
var MpfcSelect = pfcCreate("MpfcSelect");
for (var i = 0; i < 3; i++)
{
    var asmItem = subassembly.GetItemByName(pfcCreate("pfcModelItemType").ITEM_SURFACE, asmDatums[i]);
    
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
    var compItem = componentModel.GetItemByName(pfcCreate("pfcModelItemType").ITEM_SURFACE, compDatums[i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
    var asmSel = MpfcSelect.CreateModelItemSelection(asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection(compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create(pfcCreate("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
    constr.AssemblyReference = asmSel;
    constr.ComponentReference = compSel;
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (false, false);
    constrs.Append(constr);
}
asmcomp.SetConstraints(constrs, void null);
}
// 以上為 three_plane_assembly() 函式
//
// 假如 Creo 所在的操作系統不是 Windows 環境
if (!pfcIsWindows())
// 則啟動對應的 UniversalXPConnect 執行權限 (等同 Windows 下的 ActiveX)
netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
// pfcGetProESession() 是位於 pfcUtils.js 中的函式, 確定此 JavaScript 是在嵌入式瀏覽器中執行
var session = pfcGetProESession();
// 設定 config option, 不要使用元件組立流程中內建的假設約束條件
session.SetConfigOption("comp_placement_assumptions","no");
// 建立擺放零件的位置矩陣, Pro/Web.Link 中的變數無法直接建立, 必須透過 pfcCreate() 建立
var identityMatrix = pfcCreate("pfcMatrix3D");
// 建立 identity 位置矩陣
for (var x = 0; x < 4; x++)
for (var y = 0; y < 4; y++)
{
    if (x == y)
        identityMatrix.Set(x, y, 1.0);
    else
        identityMatrix.Set(x, y, 0.0);
}
// 利用 identityMatrix 建立 transf 座標轉換矩陣
var transf = pfcCreate("pfcTransform3D").Create(identityMatrix);
// 取得目前的工作目錄
var currentDir = session.getCurrentDirectory();
// 以目前已開檔的空白組立檔案, 作為 model
var model = session.CurrentModel;
// 查驗有無 model, 或 model 類別是否為組立件, 若不符合條件則丟出錯誤訊息
if (model == void null || model.Type != pfcCreate("pfcModelType").MDL_ASSEMBLY)
throw new Error (0, "Current model is not an assembly.");
// 將此模型設為組立物件
var assembly = model;

/**---------------------- LEGO_BODY--------------------**/
// 設定零件的 descriptor 物件變數
var descr = pfcCreate("pfcModelDescriptor").CreateFromFileName("v:/home/lego/man/LEGO_BODY.prt");
// 若零件在 session 則直接取用
var componentModel = session.GetModelFromDescr(descr);
// 若零件不在 session 則從工作目錄中載入 session
var componentModel = session.RetrieveModel(descr);
// 若零件已經在 session 中則放入組立檔中
if (componentModel != void null)
{
    // 注意這個 asmcomp 即為設定約束條件的本體
    // asmcomp 為特徵物件, 直接將零件, 以 transf 座標轉換矩陣方位放入組立檔案中
    var asmcomp = assembly.AssembleComponent(componentModel, transf);
}

// 建立約束條件變數
var constrs = pfcCreate("pfcComponentConstraints");
// 設定組立檔中的三個定位面, 注意內定名稱與 Pro/E WF 中的 ASM_D_FRONT 不同, 而是 ASM_FRONT, 可在組立件->info->model 中查詢定位面名稱
// 組立檔案中的 Datum 名稱也可以利用 View->plane tag display 查詢名稱
// 建立組立參考面所組成的陣列
var asmDatums = new Array("ASM_FRONT", "ASM_TOP", "ASM_RIGHT");
// 設定零件檔中的三個定位面, 名稱與 Pro/E WF 中相同
var compDatums = new Array("FRONT", "TOP", "RIGHT");
// 建立 ids 變數, intseq 為 sequence of integers 為資料類別, 使用者可以經由整數索引擷取此資料類別的元件, 第一個索引為 0
       // intseq 等同 Python 的數列資料?
var ids = pfcCreate("intseq");
// 利用 assembly 物件模型, 建立路徑變數
var path = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
// 採用互動式設定相關的變數, MpfcSelect 為 Module level class 中的一種
var MpfcSelect = pfcCreate("MpfcSelect");
// 利用迴圈分別約束組立與零件檔中的三個定位平面
for (var i = 0; i < 3; i++)
{
// 設定組立參考面, 也就是 "ASM_FRONT", "ASM_TOP", "ASM_RIGHT" 等三個 datum planes
var asmItem = assembly.GetItemByName (pfcCreate("pfcModelItemType").ITEM_SURFACE, asmDatums[i]);
// 若無對應的組立參考面, 則啟用互動式平面選擇表單 flag
if (asmItem == void null)
{
    interactFlag = true;
    continue;
}
// 設定零件參考面, 也就是 "FRONT", "TOP", "RIGHT" 等三個 datum planes
var compItem = componentModel.GetItemByName (pfcCreate ("pfcModelItemType").ITEM_SURFACE, compDatums[i]);
// 若無對應的零件參考面, 則啟用互動式平面選擇表單 flag
if (compItem == void null)
{
    interactFlag = true;
    continue;
}
        // 因為 asmItem 為組立件中的定位特徵, 必須透過 path 才能取得
var asmSel = MpfcSelect.CreateModelItemSelection(asmItem, path);
        // 而 compItem 則為零件, 沒有 path 路徑, 因此第二變數為 null
var compSel = MpfcSelect.CreateModelItemSelection(compItem, void null);
        // 利用 ASM_CONSTRAINT_ALIGN 對齊組立約束建立約束變數
var constr = pfcCreate("pfcComponentConstraint").Create (pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN);
        // 設定約束條件的組立參考與元件參考選擇
constr.AssemblyReference = asmSel;
constr.ComponentReference = compSel;
       // 第一個變數為強制變數, 第二個為忽略變數
       // 強制變數為 false, 表示不強制約束, 只有透過點與線對齊時需設為 true
       // 忽略變數為 false, 約束條件在更新模型時是否忽略, 設為 false 表示不忽略
       // 通常在組立 closed chain 機構時,  忽略變數必須設為 true, 才能完成約束
       // 因為三個面絕對約束, 因此輸入變數為 false, false
constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (false, false);
// 將互動選擇相關資料, 附加在程式約束變數之後
constrs.Append(constr);
}

// 設定組立約束條件
asmcomp.SetConstraints (constrs, void null);
/**---------------------- LEGO_ARM_RT 右手上臂--------------------**/
var descr = pfcCreate ("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/LEGO_ARM_RT.prt");
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
        // 注意這個 asmcomp 即為設定約束條件的本體
        // asmcomp 為特徵物件,直接將零件, 以 transf 座標轉換放入組立檔案中
var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
// 取得 assembly 項下的元件 id, 因為只有一個零件, 採用 index 0 取出其 featID
var components = assembly.ListFeaturesByType(true, pfcCreate ("pfcFeatureType").FEATTYPE_COMPONENT);
// 此一 featID 為組立件中的第一個零件編號, 也就是樂高人偶的 body
var featID = components.Item(0).Id;

ids.Append(featID);
// 在 assembly 模型中建立子零件所對應的路徑
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
// 以下針對 body 的 A_13 軸與 DTM1 基準面及右臂的  A_4 軸線與 DTM1 進行對齊與面接約束
var asmDatums = new Array("A_13", "DTM1");
var compDatums = new Array("A_4", "DTM1");
// 組立的關係變數為對齊與面接
var relation = new Array (pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN, pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
// 組立元件則為軸與平面
var relationItem = new Array(pfcCreate("pfcModelItemType").ITEM_AXIS, pfcCreate("pfcModelItemType").ITEM_SURFACE);
// 建立約束條件變數, 軸採對齊而基準面則以面接進行約束
var constrs = pfcCreate ("pfcComponentConstraints");
for (var i = 0; i < 2; i++)
{
                  // 設定組立參考面, asmItem 為 model item
    var asmItem = subassembly.GetItemByName (relationItem[i], asmDatums [i]);
                  // 若無對應的組立參考面, 則啟用互動式平面選擇表單 flag
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 設定零件參考面, compItem 為 model item
    var compItem = componentModel.GetItemByName (relationItem[i], compDatums[i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 採用互動式設定相關的變數
    var MpfcSelect = pfcCreate ("MpfcSelect");
    var asmSel = MpfcSelect.CreateModelItemSelection (asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection (compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create (relation[i]);
    constr.AssemblyReference  = asmSel;
    constr.ComponentReference = compSel;
                  // 因為透過軸線對齊, 第一 force 變數需設為 true
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (true, false);
                  // 將互動選擇相關資料, 附加在程式約束變數之後
    constrs.Append(constr);
}
// 設定組立約束條件, 以 asmcomp 特徵進行約束條件設定
// 請注意, 第二個變數必須為 void null 表示零件對零件進行約束, 若為 subPath, 則零件會與原始零件的平面進行約束
asmcomp.SetConstraints (constrs, void null);
/**---------------------- LEGO_ARM_LT 左手上臂--------------------**/
var descr = pfcCreate ("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/LEGO_ARM_LT.prt");
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
        // 注意這個 asmcomp 即為設定約束條件的本體
        // asmcomp 為特徵物件,直接將零件, 以 transf 座標轉換放入組立檔案中
var asmcomp = assembly.AssembleComponent(componentModel, transf);
}
// 取得 assembly 項下的元件 id, 因為只有一個零件, 採用 index 0 取出其 featID
var components = assembly.ListFeaturesByType(true, pfcCreate ("pfcFeatureType").FEATTYPE_COMPONENT);
var ids = pfcCreate ("intseq");
// 因為左臂也是與 body 進行約束條件組立,  因此取 body 的 featID
// 至此右臂 id 應該是 featID+1, 而左臂則是 featID+2
ids.Append(featID);
// 在 assembly 模型中建立子零件所對應的路徑
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
var asmDatums = new Array("A_9", "DTM2");
var compDatums = new Array("A_4", "DTM1");
var relation = new Array (pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN, pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
var relationItem = new Array(pfcCreate("pfcModelItemType").ITEM_AXIS, pfcCreate("pfcModelItemType").ITEM_SURFACE);
// 建立約束條件變數
var constrs = pfcCreate ("pfcComponentConstraints");
for (var i = 0; i < 2; i++)
{
                  // 設定組立參考面, asmItem 為 model item
    var asmItem = subassembly.GetItemByName (relationItem[i], asmDatums [i]);
                  // 若無對應的組立參考面, 則啟用互動式平面選擇表單 flag
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 設定零件參考面, compItem 為 model item
    var compItem = componentModel.GetItemByName (relationItem[i], compDatums [i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 採用互動式設定相關的變數
    var MpfcSelect = pfcCreate ("MpfcSelect");
    var asmSel = MpfcSelect.CreateModelItemSelection (asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection (compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create (relation[i]);
    constr.AssemblyReference  = asmSel;
    constr.ComponentReference = compSel;
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (true, false);
                  // 將互動選擇相關資料, 附加在程式約束變數之後
    constrs.Append(constr);
}
// 設定組立約束條件, 以 asmcomp 特徵進行約束條件設定
// 請注意, 第二個變數必須為 void null 表示零件對零件進行約束, 若為 subPath, 則零件會與原始零件的平面進行約束
asmcomp.SetConstraints (constrs, void null);
/**---------------------- LEGO_HAND 右手手腕--------------------**/
// 右手臂 LEGO_ARM_RT.prt 基準  A_2, DTM2
// 右手腕 LEGO_HAND.prt 基準 A_1, DTM3
var descr = pfcCreate ("pfcModelDescriptor").CreateFromFileName ("v:/home/lego/man/LEGO_HAND.prt");
var componentModel = session.GetModelFromDescr(descr);
var componentModel = session.RetrieveModel(descr);
if (componentModel != void null)
{
        // 注意這個 asmcomp 即為設定約束條件的本體
        // asmcomp 為特徵物件,直接將零件, 以 transf 座標轉換放入組立檔案中
var asmcomp = assembly.AssembleComponent (componentModel, transf);
}
// 取得 assembly 項下的元件 id, 因為只有一個零件, 採用 index 0 取出其 featID
var components = assembly.ListFeaturesByType(true, pfcCreate ("pfcFeatureType").FEATTYPE_COMPONENT);
var ids = pfcCreate ("intseq");

// 組立件中 LEGO_BODY.prt 編號為 featID
// LEGO_ARM_RT.prt 則是組立件第二個置入的零件,  編號為 featID+1
ids.Append(featID+1);
// 在 assembly 模型中, 根據子零件的編號, 建立子零件所對應的路徑
var subPath = pfcCreate("MpfcAssembly").CreateComponentPath(assembly, ids);
subassembly = subPath.Leaf;
// 以下針對 LEGO_ARM_RT 的 A_2 軸與 DTM2 基準面及 HAND 的  A_1 軸線與 DTM3 進行對齊與面接約束
var asmDatums = new Array("A_2", "DTM2");
var compDatums = new Array("A_1", "DTM3");
// 組立的關係變數為對齊與面接
var relation = new Array (pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_ALIGN, pfcCreate ("pfcComponentConstraintType").ASM_CONSTRAINT_MATE);
// 組立元件則為軸與平面
var relationItem = new Array(pfcCreate("pfcModelItemType").ITEM_AXIS, pfcCreate("pfcModelItemType").ITEM_SURFACE);
// 建立約束條件變數, 軸採對齊而基準面則以面接進行約束
var constrs = pfcCreate ("pfcComponentConstraints");
for (var i = 0; i < 2; i++)
{
                  // 設定組立參考面, asmItem 為 model item
    var asmItem = subassembly.GetItemByName (relationItem[i], asmDatums [i]);
                  // 若無對應的組立參考面, 則啟用互動式平面選擇表單 flag
    if (asmItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 設定零件參考面, compItem 為 model item
    var compItem = componentModel.GetItemByName (relationItem[i], compDatums [i]);
    if (compItem == void null)
    {
        interactFlag = true;
        continue;
    }
                  // 採用互動式設定相關的變數
    var MpfcSelect = pfcCreate("MpfcSelect");
    var asmSel = MpfcSelect.CreateModelItemSelection(asmItem, subPath);
    var compSel = MpfcSelect.CreateModelItemSelection (compItem, void null);
    var constr = pfcCreate("pfcComponentConstraint").Create (relation[i]);
    constr.AssemblyReference  = asmSel;
    constr.ComponentReference = compSel;
                  // 因為透過軸線對齊, 第一 force 變數需設為 true
    constr.Attributes = pfcCreate("pfcConstraintAttributes").Create (true, false);
                  // 將互動選擇相關資料, 附加在程式約束變數之後
    constrs.Append(constr);
}
// 設定組立約束條件, 以 asmcomp 特徵進行約束條件設定
// 請注意, 第二個變數必須為 void null 表示零件對零件進行約束, 若為 subPath, 則零件會與原始零件的平面進行約束
asmcomp.SetConstraints (constrs, void null);
// 利用函式呼叫組立左手 HAND
axis_plane_assembly(session, assembly, transf, featID, 2, 
                              "LEGO_HAND.prt", "A_2", "DTM2", "A_1", "DTM3");
// 利用函式呼叫組立人偶頭部 HEAD
// BODY id 為 featID+0, 以 A_2 及  DTM3 約束
// HEAD 則直接呼叫檔案名稱, 以 A_2, DTM2 約束
axis_plane_assembly(session, assembly, transf, featID, 0, 
                              "LEGO_HEAD.prt", "A_2", "DTM3", "A_2", "DTM2");
// Body 與 WAIST 採三個平面約束組立
// Body 組立面為 DTM4, DTM5, DTM6
// WAIST 組立面為 DTM1, DTM2, DTM3
three_plane_assembly(session, assembly, transf, featID, 0, "LEGO_WAIST.prt", "DTM4", "DTM5", "DTM6", "DTM1", "DTM2", "DTM3"); 
// 右腳
axis_plane_assembly(session, assembly, transf, featID, 6, 
                              "LEGO_LEG_RT.prt", "A_8", "DTM4", "A_10", "DTM1");
// 左腳
axis_plane_assembly(session, assembly, transf, featID, 6, 
                              "LEGO_LEG_LT.prt", "A_8", "DTM5", "A_10", "DTM1");
// 紅帽
axis_plane_assembly(session, assembly, transf, featID, 5, 
                              "LEGO_HAT.prt", "A_2", "TOP", "A_2", "FRONT");
// regenerate 並且 repaint 組立檔案
assembly.Regenerate (void null);
session.GetModelWindow (assembly).Repaint();    
</script>
</body>
</html>
'''
        return outstring
def downloadlist_access_list(files, starti, endi):
    # different extension files, associated links were provided
    # popup window to view images, video or STL files, other files can be downloaded directly
    # files are all the data to list, from starti to endi
    # add file size
    outstring = ""
    for index in range(int(starti)-1, int(endi)):
        fileName, fileExtension = os.path.splitext(files[index])
        fileExtension = fileExtension.lower()
        fileSize = sizeof_fmt(os.path.getsize(download_root_dir+"downloads/"+files[index]))
        # images files
        if fileExtension == ".png" or fileExtension == ".jpg" or fileExtension == ".gif":
            outstring += '<input type="checkbox" name="filename" value="'+files[index]+'"><a href="javascript:;" onClick="window.open(\'/downloads/'+ \
            files[index]+'\',\'images\', \'catalogmode\',\'scrollbars\')">'+files[index]+'</a> ('+str(fileSize)+')<br />'
        # stl files
        elif fileExtension == ".stl":
            outstring += '<input type="checkbox" name="filename" value="'+files[index]+'"><a href="javascript:;" onClick="window.open(\'/static/viewstl.html?src=/downloads/'+ \
            files[index]+'\',\'images\', \'catalogmode\',\'scrollbars\')">'+files[index]+'</a> ('+str(fileSize)+')<br />'
        # flv files
        elif fileExtension == ".flv":
            outstring += '<input type="checkbox" name="filename" value="'+files[index]+'"><a href="javascript:;" onClick="window.open(\'/flvplayer?filepath=/downloads/'+ \
            files[index]+'\',\'images\', \'catalogmode\',\'scrollbars\')">'+files[index]+'</a> ('+str(fileSize)+')<br />'
        # direct download files
        else:
            outstring += "<input type='checkbox' name='filename' value='"+files[index]+"'><a href='/download/?filepath="+download_root_dir.replace('\\', '/')+ \
            "downloads/"+files[index]+"'>"+files[index]+"</a> ("+str(fileSize)+")<br />"
    return outstring
def sizeof_fmt(num):
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')
################# (3) 程式類別定義區
# 以下改用 CherryPy 網際框架程式架構
# 以下為 Hello 類別的設計內容, 其中的 object 使用, 表示 Hello 類別繼承 object 的所有特性, 包括方法與屬性設計
class Midterm(object):

    # Midterm 類別的啟動設定
    _cp_config = {
    'tools.encode.encoding': 'utf-8',
    'tools.sessions.on' : True,
    'tools.sessions.storage_type' : 'file',
    #'tools.sessions.locking' : 'explicit',
    # session 以檔案儲存, 而且位於 data_dir 下的 tmp 目錄
    'tools.sessions.storage_path' : data_dir+'/tmp',
    # session 有效時間設為 60 分鐘
    'tools.sessions.timeout' : 60
    }

    def __init__(self):
        # hope to create downloads and images directories　
        if not os.path.isdir(download_root_dir+"downloads"):
            try:
                os.makedirs(download_root_dir+"downloads")
            except:
                print("mkdir error")
        if not os.path.isdir(download_root_dir+"images"):
            try:
                os.makedirs(download_root_dir+"images")
            except:
                print("mkdir error")
        if not os.path.isdir(download_root_dir+"tmp"):
            try:
                os.makedirs(download_root_dir+"tmp")
            except:
                print("mkdir error")
    @cherrypy.expose
    def index(self, N=20 ,N1=20 , M=4, P=20,midx=400):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">
        
    <h2><span style="color:blue;">cda_g2 40223106課程練習</span><h2><br />

    <span style="color:orange;">cda_g2_w11 練習</span><br />
    <br />

    <form method=POST action=index>
    <a href="spur">spur</a>  &nbsp; &nbsp; &nbsp;
    <a href="drawspur">drawspur</a><br /><br /><br />
    <a href="fileuploadform">上傳檔案</a>&nbsp; &nbsp; &nbsp;
    <a href="download_list">列出上傳檔案</a><br />

    <table  style="border:3px #FFAC55 dashed;padding:5px;" rules="all" cellpadding='5';><tr>
    　<td>cda第二組</td></tr>
    </table><br />

    <table  style="border:3px #FFAC55 double;padding:5px;" rules="all" cellpadding='5';>
    <tr><td>超猛組長</td><td>40223131</td><td>陳柏安</td></tr>
    <tr><td>組員</td><td>40223102</td><td>吳佳容</td></tr>
    <tr><td>組員</td><td>40223104</td><td>林瑩禎</td></tr>
    <tr><td>組員</td><td>40223105</td><td>侯云婷</td></tr>
    <tr><td>組員</td><td>40223106</td><td>許芸瑄</td></tr>
    <tr><td>組員</td><td>40223107</td><td>黃雯琦</td></tr>
    <tr><td>組員</td><td>40023107</td><td>陳儀芳</td></tr>
    </table>


    '''
        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def spur(self, N=20 , M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">

    <h1>cda_g2_w11 練習</h1>

    <form method=POST action=spuraction>
    齒數:<select name"select_one>
    <option value="20">20</option>
    <option value="25">25</option>
    <option value="30">30</option>
    <option value="35">35</option>
    <option value="40">40</option>
    <option value="35">35</option>
    </select><br />
    模數:<select name"select_two>
    <option value="5">5</option>
    <option value="10">10</option>
    <option value="15">15</option>
    </select><br />
    壓力角:<select name"select_three>
    <option value="15">15</option>
    <option value="20">20</option>
    </select><br />
    <input type=submit value=send>

    </form>
    <hr>

    '''

        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def spuraction(self, N=20 , M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">

    齒數:'''+str(N)+'''<output name=N for=str(N)><br />
    模數:'''+str(M)+'''<output name=M for=str(M)><br />
    壓力角:'''+str(P)+'''<output name=P for=str(P)><br />
    '''

        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def drawspur(self, N=20, N1=10, N2=30, N3=10, N4=20, N5=30, N6=30,M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">

    <form method=POST action=drawspuraction>
    第1齒數:<input type=text name=N><br />
    第2齒數:<input type=text name=N1><br />
    第3齒數:<input type=text name=N2><br />
    第4齒數:<input type=text name=N3><br />
    第5齒數:<input type=text name=N4><br />
    第6齒數:<input type=text name=N5><br />
    第7齒數:<input type=text name=N6><br />
    模數:<input type=text name=M><br />
    壓力角:<input type=text name=P><br />
    <input type=submit value=send>



    '''

        return outstring
    @cherrypy.expose
    # N 為齒數, M 為模數, P 為壓力角
    def drawspuraction(self, N=20, N1=10, N2=30, N3=10, N4=20, N5=30, N6=30,M=5, P=15):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    <script src="/static/Cango2D.js" type="text/javascript"></script>
    <script src="/static/gearUtils-04.js" type="text/javascript"></script>
    </head>
    <!-- 啟動 brython() -->
    <body onload="brython()">

    第1齒數:'''+str(N)+'''<output name=N for=str(N)><br />
    第2齒數:'''+str(N1)+'''<output name=N1 for=str(N1)><br />
    第3齒數:'''+str(N2)+'''<output name=N2 for=str(N2)><br />
    第4齒數:'''+str(N3)+'''<output name=N3 for=str(N3)><br />
    第5齒數:'''+str(N4)+'''<output name=N4 for=str(N4)><br />
    第6齒數:'''+str(N5)+'''<output name=N5 for=str(N5)><br />
    第7齒數:'''+str(N6)+'''<output name=N5 for=str(N6)><br />
    模數:'''+str(M)+'''<output name=M for=str(M)><br />
    壓力角:'''+str(P)+'''<output name=P for=str(P)><br />
    齒數比:'''+str(N)+''':'''+str(N1)+''':'''+str(N2)+''':'''+str(N3)+''':'''+str(N4)+''':'''+str(N5)+''':'''+str(N6)+'''<br />

    <!-- 以下為 canvas 畫圖程式 -->
    <script type="text/python">
    # 從 browser 導入 document
    from browser import document
    from math import *
    # 請注意, 這裡導入位於 Lib/site-packages 目錄下的 spur.py 檔案
    import spur

    # 準備在 id="plotarea" 的 canvas 中繪圖
    canvas = document["plotarea"]
    ctx = canvas.getContext("2d")

    # 以下利用 spur.py 程式進行繪圖, 接下來的協同設計運算必須要配合使用者的需求進行設計運算與繪圖
    # 其中並將工作分配給其他組員建立類似 spur.py 的相關零件繪圖模組
    # midx, midy 為齒輪圓心座標, rp 為節圓半徑, n 為齒數, pa 為壓力角, color 為線的顏色
    # Gear(midx, midy, rp, n=20, pa=20, color="black"):
    # 模數決定齒的尺寸大小, 囓合齒輪組必須有相同的模數與壓力角
    # 壓力角 pa 單位為角度
    pa = 20
    # m 為模數
    m = '''+str(M)+'''
    # 第1齒輪齒數
    n_g1 = '''+str(N)+'''
    # 第2齒輪齒數
    n_g2 = '''+str(N1)+'''
    # 第3齒輪齒數
    n_g3 ='''+str(N2)+'''
    # 第4齒輪齒數
    n_g4 ='''+str(N3)+'''
    # 第5齒輪齒數
    n_g5 ='''+str(N4)+'''
    # 第6齒輪齒數
    n_g6 ='''+str(N5)+'''
    # 第7齒輪齒數
    n_g7 ='''+str(N6)+'''



    # 計算兩齒輪的節圓半徑
    rp_g1 = m*n_g1/2
    rp_g2 = m*n_g2/2
    rp_g3 = m*n_g3/2
    rp_g4 = m*n_g4/2
    rp_g5= m*n_g5/2
    rp_g6= m*n_g6/2
    rp_g7= m*n_g7/2

    # 繪圖第1齒輪的圓心座標
    x_g1 = 400
    y_g1 = 400
    # 第2齒輪的圓心座標, 假設排列成水平, 表示各齒輪圓心 y 座標相同
    x_g2 = x_g1 + rp_g1 + rp_g2
    y_g2 = y_g1
    # 第3齒輪的圓心座標
    x_g3 = x_g1 + rp_g1 + 2*rp_g2 + rp_g3
    y_g3 = y_g1

    # 第4齒輪的圓心座標
    x_g4 = x_g1 + rp_g1 + 2*rp_g2 + 2* rp_g3 + rp_g4
    y_g4 = y_g1

    # 第5齒輪的圓心座標
    x_g5= x_g1 + rp_g1 + 2*rp_g2 + 2* rp_g3 +2* rp_g4+ rp_g5
    y_g5 = y_g1

    # 第6齒輪的圓心座標
    x_g6= x_g1 + rp_g1 + 2*rp_g2 + 2* rp_g3 +2* rp_g4+2* rp_g5+rp_g6
    y_g6= y_g1

    # 第7齒輪的圓心座標
    x_g7= x_g1 + rp_g1 + 2*rp_g2 + 2* rp_g3 +2* rp_g4+2* rp_g5+2*rp_g6+rp_g7
    y_g7= y_g1


    # 將第1齒輪順時鐘轉 90 度
    # 使用 ctx.save() 與 ctx.restore() 以確保各齒輪以相對座標進行旋轉繪圖

    ctx.font = "10px Verdana";
    ctx.fillText("組員:31",x_g1-20, y_g1-10);

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g1, y_g1)
    # rotate to engage
    ctx.rotate(pi/2)
    # put it back
    ctx.translate(-x_g1, -y_g1)
    spur.Spur(ctx).Gear(x_g1, y_g1, rp_g1, n_g1, pa, "blue")
    ctx.restore()

    # 將第2齒輪逆時鐘轉 90 度之後, 再多轉一齒, 以便與第1齒輪進行囓合

    ctx.font = "10px Verdana";
    ctx.fillText("組員:04",x_g2-20, y_g2-10);

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g2, y_g2)
    # rotate to engage
    ctx.rotate(-pi/2-pi/n_g2)
    # put it back
    ctx.translate(-x_g2, -y_g2)
    spur.Spur(ctx).Gear(x_g2, y_g2, rp_g2, n_g2, pa, "black")
    ctx.restore()

    # 將第3齒輪逆時鐘轉 90 度之後, 再往回轉第2齒輪定位帶動轉角, 然後再逆時鐘多轉一齒, 以便與第2齒輪進行囓合

    ctx.font = "10px Verdana";
    ctx.fillText("組員:07",x_g3-20, y_g3-10);

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g3, y_g3)
    # rotate to engage
    # pi+pi/n_g2 為第2齒輪從順時鐘轉 90 度之後, 必須配合目前的標記線所作的齒輪 2 轉動角度, 要轉換到齒輪3 的轉動角度
    # 必須乘上兩齒輪齒數的比例, 若齒輪2 大, 則齒輪3 會轉動較快
    # 第1個 -pi/2 為將原先垂直的第3齒輪定位線逆時鐘旋轉 90 度
    # -pi/n_g3 則是第3齒與第2齒定位線重合後, 必須再逆時鐘多轉一齒的轉角, 以便進行囓合
    # (pi+pi/n_g2)*n_g2/n_g3 則是第2齒原定位線為順時鐘轉動 90 度, 
    # 但是第2齒輪為了與第1齒輪囓合, 已經距離定位線, 多轉了 180 度, 再加上第2齒輪的一齒角度, 因為要帶動第3齒輪定位, 
    # 這個修正角度必須要再配合第2齒與第3齒的轉速比加以轉換成第3齒輪的轉角, 因此乘上 n_g2/n_g3
    ctx.rotate(-pi/2-pi/n_g3+(pi+pi/n_g2)*n_g2/n_g3)
    # put it back
    ctx.translate(-x_g3, -y_g3)
    spur.Spur(ctx).Gear(x_g3, y_g3, rp_g3, n_g3, pa, "red")
    ctx.restore()

    # 按照上面三個正齒輪的囓合轉角運算, 隨後的傳動齒輪轉角便可依此類推, 完成6個齒輪的囓合繪圖

    #第4齒輪

    ctx.font = "10px Verdana";
    ctx.fillText("組員:02",x_g4-20, y_g4-10);

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g4, y_g4)
    # rotate to engage
    ctx.rotate(-pi/2-pi/n_g4+(pi+pi/n_g3)*n_g3/n_g4-(pi+pi/n_g2)*n_g2/n_g4)
    # put it back
    ctx.translate(-x_g4, -y_g4)
    spur.Spur(ctx).Gear(x_g4, y_g4, rp_g4, n_g4, pa, "green")
    ctx.restore()

    #第5齒輪

    ctx.font = "10px Verdana";
    ctx.fillText("組員:06",x_g5-20, y_g5+10);

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g5, y_g5)
    # rotate to engage
    ctx.rotate(-pi/2-pi/n_g5+(pi+pi/n_g4)*n_g4/n_g5-(pi+pi/n_g3)*n_g3/n_g5+(pi+pi/n_g2)*n_g2/n_g5)
    # put it back
    ctx.translate(-x_g5, -y_g5)
    spur.Spur(ctx).Gear(x_g5, y_g5, rp_g5, n_g5, pa, "purple")
    ctx.restore()

    #第6齒輪

    ctx.font = "10px Verdana";
    ctx.fillText("組員:05",x_g6-20, y_g6+10);

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g6, y_g6)
    # rotate to engage
    ctx.rotate(-pi/2-pi/n_g6+(pi+pi/n_g5)*n_g5/n_g6-
    (pi+pi/n_g4)*n_g4/n_g6+(pi+pi/n_g3)*n_g3/n_g6-
    (pi+pi/n_g2)*n_g2/n_g6)
    # put it back
    ctx.translate(-x_g6, -y_g6)
    spur.Spur(ctx).Gear(x_g6, y_g6, rp_g6, n_g6, pa, "blue")
    ctx.restore()

    #第7齒輪

    ctx.font = "10px Verdana";
    ctx.fillText("組員:40023107",x_g7-20, y_g7+10);

    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g7, y_g7)
    # rotate to engage
    ctx.rotate(-pi/2-pi/n_g7+(pi+pi/n_g6)*n_g6/n_g7-
    (pi+pi/n_g5)*n_g5/n_g7+(pi+pi/n_g4)*n_g4/n_g7-
    (pi+pi/n_g3)*n_g3/n_g7+(pi+pi/n_g2)*n_g2/n_g7)
    # put it back
    ctx.translate(-x_g7, -y_g7)
    spur.Spur(ctx).Gear(x_g7, y_g7, rp_g7, n_g7, pa, "Brown")
    ctx.restore()

    </script>
    <canvas id="plotarea" width="3000" height="3000"></canvas>
    </body>
    </html>
    '''

        return outstring
    '''

    # 第5齒輪的圓心座標
    x_g5= x_g1 + rp_g1 + 2*rp_g2 + 2* rp_g3 +2* rp_g4+ rp_g5
    y_g5 = y_g1

    # 第6齒輪的圓心座標
    x_g6= x_g1 + rp_g1 + 2*rp_g2 + 2* rp_g3 +2* rp_g4+2* rp_g5+rp_g6
    y_g6= y_g1

    #第5齒輪
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g5, y_g5)
    # rotate to engage
    ctx.rotate(-pi-pi/n_g5+(pi+pi/n_g4)*n_g4/n_g5)
    # put it back
    ctx.translate(-x_g5, -y_g5)
    spur.Spur(ctx).Gear(x_g5, y_g5, rp_g5, n_g5, pa, "purple")
    ctx.restore()

    #第6齒輪
    ctx.save()
    # translate to the origin of second gear
    ctx.translate(x_g6, y_g6)
    # rotate to engage
    ctx.rotate(-pi/2-pi/n_g6-pi/n_g6+(pi+pi/n_g5)*n_g5/n_g6)
    # put it back
    ctx.translate(-x_g6, -y_g6)
    spur.Spur(ctx).Gear(x_g6, y_g6, rp_g6, n_g6, pa, "blue")
    ctx.restore()
    '''
    @cherrypy.expose
    # W 為正方體的邊長
    def cube(self, W=10):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
    <!-- 使用者輸入表單的參數交由 cubeaction 方法處理 -->
    <form method=POST action=cubeaction>
    正方體邊長:<input type=text name=W value='''+str(W)+'''><br />
    <input type=submit value=送出>
    </form>
    <br /><a href="index">index</a><br />
    </body>
    </html>
    '''

        return outstring
    @cherrypy.expose
    # W 為正方體邊長, 內定值為 10
    def cubeaction(self, W=10):
        outstring = '''
    <!DOCTYPE html> 
    <html>
    <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <!-- 先載入 pfcUtils.js 與 wl_header.js -->
    <script type="text/javascript" src="/static/weblink/pfcUtils.js"></script>
    <script type="text/javascript" src="/static/weblink/wl_header.js">
    <!-- 載入 brython.js -->
    <script type="text/javascript" src="/static/Brython3.1.1-20150328-091302/brython.js"></script>
    document.writeln ("Error loading Pro/Web.Link header!");
    </script>
    <script>
    window.onload=function(){
    brython();
    }
    </script>
    </head>
    <!-- 不要使用 body 啟動 brython() 改為 window level 啟動 -->
    <body onload="">
    <h1>Creo 參數化零件</h1>
    <a href="index">index</a><br />

    <!-- 以下為 Creo Pro/Web.Link 程式, 將 JavaScrip 改為 Brython 程式 -->

    <script type="text/python">
    from browser import document, window
    from math import *

    # 這個區域為 Brython 程式範圍, 註解必須採用 Python 格式
    # 因為 pfcIsWindows() 為原生的 JavaScript 函式, 在 Brython 中引用必須透過 window 物件
    if (!window.pfcIsWindows()) window.netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
    # 若第三輸入為 false, 表示僅載入 session, 但是不顯示
    # ret 為 model open return
    ret = document.pwl.pwlMdlOpen("cube.prt", "v:/tmp", false)
    if (!ret.Status):
        window.alert("pwlMdlOpen failed (" + ret.ErrorCode + ")")
        # 將 ProE 執行階段設為變數 session
        session = window.pfcGetProESession()
        # 在視窗中打開零件檔案, 並且顯示出來
        pro_window = session.OpenFile(pfcCreate("pfcModelDescriptor").CreateFromFileName("cube.prt"))
        solid = session.GetModel("cube.prt", window.pfcCreate("pfcModelType").MDL_PART)
        # 在 Brython 中與 Python 語法相同, 只有初值設定問題, 無需宣告變數
        # length, width, myf, myn, i, j, volume, count, d1Value, d2Value
        # 將模型檔中的 length 變數設為 javascript 中的 length 變數
        length = solid.GetParam("a1")
        # 將模型檔中的 width 變數設為 javascript 中的 width 變數
        width = solid.GetParam("a2")
        # 改變零件尺寸
        # myf=20
        # myn=20
        volume = 0
        count = 0
        try:
            # 以下採用 URL 輸入對應變數
            # createParametersFromArguments ();
            # 以下則直接利用 javascript 程式改變零件參數
            for i in range(5):
                myf ='''+str(W)+'''
                myn ='''+str(W)+''' + i*2.0
                # 設定變數值, 利用 ModelItem 中的 CreateDoubleParamValue 轉換成 Pro/Web.Link 所需要的浮點數值
                d1Value = window.pfcCreate ("MpfcModelItem").CreateDoubleParamValue(myf)
                d2Value = window.pfcCreate ("MpfcModelItem").CreateDoubleParamValue(myn)
                # 將處理好的變數值, 指定給對應的零件變數
                length.Value = d1Value
                width.Value = d2Value
                # 零件尺寸重新設定後, 呼叫 Regenerate 更新模型
                # 在 JavaScript 為 null 在 Brython 為 None
                solid.Regenerate(None)
                # 利用 GetMassProperty 取得模型的質量相關物件
                properties = solid.GetMassProperty(None)
                # volume = volume + properties.Volume
                volume = properties.Volume
                count = count + 1
                window.alert("執行第"+count+"次,零件總體積:"+volume)
                # 將零件存為新檔案
                newfile = document.pwl.pwlMdlSaveAs("cube.prt", "v:/tmp", "cube"+count+".prt")
                if (!newfile.Status):
                    window.alert("pwlMdlSaveAs failed (" + newfile.ErrorCode + ")")
                # window.alert("共執行:"+count+"次,零件總體積:"+volume)
                # window.alert("零件體積:"+properties.Volume)
                # window.alert("零件體積取整數:"+Math.round(properties.Volume));
        except:
            window.alert ("Exception occurred: "+window.pfcGetExceptionType (err))
    </script>
    '''

        return outstring
    @cherrypy.expose
    def fileuploadform(self):
        return '''<h1>file upload</h1>
    <script src="/static/jquery.js" type="text/javascript"></script>
    <script src="/static/axuploader.js" type="text/javascript"></script>
    <script>
    $(document).ready(function(){
    $('.prova').axuploader({url:'fileaxupload', allowExt:['jpg','png','gif','7z','pdf','zip','flv','stl','swf'],
    finish:function(x,files)
        {
            alert('All files have been uploaded: '+files);
        },
    enable:true,
    remotePath:function(){
    return 'downloads/';
    }
    });
    });
    </script>
    <div class="prova"></div>
    <input type="button" onclick="$('.prova').axuploader('disable')" value="asd" />
    <input type="button" onclick="$('.prova').axuploader('enable')" value="ok" />
    </section></body></html>
    '''
    @cherrypy.expose
    def fileaxupload(self, *args, **kwargs):
        filename = kwargs["ax-file-name"]
        flag = kwargs["start"]
        if flag == "0":
            file = open(download_root_dir+"downloads/"+filename, "wb")
        else:
            file = open(download_root_dir+"downloads/"+filename, "ab")
        file.write(cherrypy.request.body.read())
        file.close()
        return "files uploaded!"
    @cherrypy.expose
    def download_list(self, item_per_page=5, page=1, keyword=None, *args, **kwargs):
        files = os.listdir(download_root_dir+"downloads/")
        total_rows = len(files)
        totalpage = math.ceil(total_rows/int(item_per_page))
        starti = int(item_per_page) * (int(page) - 1) + 1
        endi = starti + int(item_per_page) - 1
        outstring = "<form method='post' action='delete_file'>"
        notlast = False
        if total_rows > 0:
            outstring += "<br />"
            if (int(page) * int(item_per_page)) < total_rows:
                notlast = True
            if int(page) > 1:
                outstring += "<a href='"
                outstring += "download_list?&amp;page=1&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'><<</a> "
                page_num = int(page) - 1
                outstring += "<a href='"
                outstring += "download_list?&amp;page="+str(page_num)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>Previous</a> "
            span = 10
            for index in range(int(page)-span, int(page)+span):
                if index>= 0 and index< totalpage:
                    page_now = index + 1 
                    if page_now == int(page):
                        outstring += "<font size='+1' color='red'>"+str(page)+" </font>"
                    else:
                        outstring += "<a href='"
                        outstring += "download_list?&amp;page="+str(page_now)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                        outstring += "'>"+str(page_now)+"</a> "

            if notlast == True:
                nextpage = int(page) + 1
                outstring += " <a href='"
                outstring += "download_list?&amp;page="+str(nextpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>Next</a>"
                outstring += " <a href='"
                outstring += "download_list?&amp;page="+str(totalpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>>></a><br /><br />"
            if (int(page) * int(item_per_page)) < total_rows:
                notlast = True
                outstring += downloadlist_access_list(files, starti, endi)+"<br />"
            else:
                outstring += "<br /><br />"
                outstring += downloadlist_access_list(files, starti, total_rows)+"<br />"
            
            if int(page) > 1:
                outstring += "<a href='"
                outstring += "download_list?&amp;page=1&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'><<</a> "
                page_num = int(page) - 1
                outstring += "<a href='"
                outstring += "download_list?&amp;page="+str(page_num)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>Previous</a> "
            span = 10
            for index in range(int(page)-span, int(page)+span):
            #for ($j=$page-$range;$j<$page+$range;$j++)
                if index >=0 and index < totalpage:
                    page_now = index + 1
                    if page_now == int(page):
                        outstring += "<font size='+1' color='red'>"+str(page)+" </font>"
                    else:
                        outstring += "<a href='"
                        outstring += "download_list?&amp;page="+str(page_now)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                        outstring += "'>"+str(page_now)+"</a> "
            if notlast == True:
                nextpage = int(page) + 1
                outstring += " <a href='"
                outstring += "download_list?&amp;page="+str(nextpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>Next</a>"
                outstring += " <a href='"
                outstring += "download_list?&amp;page="+str(totalpage)+"&amp;item_per_page="+str(item_per_page)+"&amp;keyword="+str(cherrypy.session.get('download_keyword'))
                outstring += "'>>></a>"
        else:
            outstring += "no data!"
        outstring += "<br /><br /><input type='submit' value='delete'><input type='reset' value='reset'></form>"

        return "<div class='container'><nav>"+ \
            "</nav><section><h1>Download List</h1>"+outstring+"<br/><br /></body></html>"
class Download:
    @cherrypy.expose
    def index(self, filepath):
        return serve_file(filepath, "application/x-download", "attachment")
################# (4) 程式啟動區
# 配合程式檔案所在目錄設定靜態目錄或靜態檔案
application_conf = {'/static':{
        'tools.staticdir.on': True,
        # 程式執行目錄下, 必須自行建立 static 目錄
        'tools.staticdir.dir': _curdir+"/static"},
        '/downloads':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/downloads"},
        '/images':{
        'tools.staticdir.on': True,
        'tools.staticdir.dir': data_dir+"/images"}
    }
    
root = Midterm()
root.download = Download()
root.man = man.MAN()
root.man2 = man2.MAN()
#root.gear = gear.Gear()

if 'OPENSHIFT_REPO_DIR' in os.environ.keys():
    # 表示在 OpenSfhit 執行
    application = cherrypy.Application(root, config=application_conf)
else:
    # 表示在近端執行
    cherrypy.config.update({'server.socket_port': 8099})
    cherrypy.quickstart(root, config=application_conf)
