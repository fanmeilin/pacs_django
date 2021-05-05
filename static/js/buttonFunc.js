cornerstoneTools.external.cornerstone = cornerstone;
cornerstoneTools.external.cornerstoneMath = cornerstoneMath;
cornerstoneTools.external.Hammer = Hammer;
cornerstoneWADOImageLoader.external.dicomParser = dicomParser;
cornerstoneWADOImageLoader.external.cornerstone = cornerstone;
//'dicomweb' 'wadouri'  'http'

var imageIds = [
"wadouri:http://127.0.0.1:8000/read0",
"wadouri:http://127.0.0.1:8000/read1",
"wadouri:http://127.0.0.1:8000/read2",
"wadouri:http://127.0.0.1:8000/read3",
"wadouri:http://127.0.0.1:8000/read4",
"wadouri:http://127.0.0.1:8000/read5",
"wadouri:http://127.0.0.1:8000/read6",
"wadouri:http://127.0.0.1:8000/read7",
"wadouri:http://127.0.0.1:8000/read8",
"wadouri:http://127.0.0.1:8000/read9"];

//初始化tools
cornerstoneTools.init();
//设置stack
const stack = {
    currentImageIdIndex: 0,
    imageIds
}
//定义stack滚动工具
const StackScrollMouseWheelTool = cornerstoneTools.StackScrollMouseWheelTool;
var element = document.getElementById('dicomImage');
cornerstone.enable(element);
cornerstone.loadAndCacheImage(imageIds[0]).then(function(image) {
    cornerstone.displayImage(element, image)
    cornerstoneTools.addStackStateManager(element, ['stack'])
    cornerstoneTools.addToolState(element, 'stack', stack)
    console.log(element)
})
cornerstoneTools.addTool(StackScrollMouseWheelTool)
cornerstoneTools.setToolActive('StackScrollMouseWheel', { })

//放大器
const ZoomMouseWheelTool = cornerstoneTools.ZoomMouseWheelTool;
cornerstoneTools.addTool(ZoomMouseWheelTool)

//角度
const AngleTool = cornerstoneTools.AngleTool;
cornerstoneTools.addTool(AngleTool);

//wwwc
const WwwcTool = cornerstoneTools.WwwcTool;
cornerstoneTools.addTool(WwwcTool);

//Eraser Tool
const EraserTool = cornerstoneTools.EraserTool;
cornerstoneTools.addTool(EraserTool);

//length
const LengthTool = cornerstoneTools.LengthTool;
cornerstoneTools.addTool(LengthTool);

//探测工具
const ProbeTool = cornerstoneTools.ProbeTool;
cornerstoneTools.addTool(ProbeTool);

//拖拽探测
const DragProbeTool = cornerstoneTools.DragProbeTool;
cornerstoneTools.addTool(DragProbeTool)

//局部放大
const MagnifyTool = cornerstoneTools.MagnifyTool;
cornerstoneTools.addTool(MagnifyTool);

//旋转工具
const RotateTool = cornerstoneTools.RotateTool;
cornerstoneTools.addTool(RotateTool);

//双向工具
const BidirectionalTool = cornerstoneTools.BidirectionalTool;
cornerstoneTools.addTool(BidirectionalTool);

//柯布角测量
const CobbAngleTool = cornerstoneTools.CobbAngleTool;
cornerstoneTools.addTool(CobbAngleTool)

//绘制面积测量
const FreehandRoiTool = cornerstoneTools.FreehandRoiTool;
cornerstoneTools.addTool(FreehandRoiTool);

//矩形面积
const RectangleRoiTool = cornerstoneTools.RectangleRoiTool;
cornerstoneTools.addTool(RectangleRoiTool)

//文本标记
const TextMarkerTool = cornerstoneTools.TextMarkerTool
const configuration = {
    markers: ['F5', 'F4', 'F3', 'F2', 'F1'],
    current: 'F5',
    ascending: true,
    loop: true,
  }
  cornerstoneTools.addTool(TextMarkerTool, { configuration })

// Brush tool
const BrushTool  =  cornerstoneTools.BrushTool;
cornerstoneTools.addTool(BrushTool);

//平移图像
const PanTool = cornerstoneTools.PanTool;
cornerstoneTools.addTool(PanTool)

//箭头标识ArrowAnnotate 
const ArrowAnnotateTool = cornerstoneTools.ArrowAnnotateTool;
cornerstoneTools.addTool(ArrowAnnotateTool)

function disableAllTools(){
    cornerstoneTools.setToolDisabled('Wwwc');
    cornerstoneTools.setToolDisabled('Angle');
    cornerstoneTools.setToolDisabled('Length');
    cornerstoneTools.setToolDisabled('Eraser');
    cornerstoneTools.setToolDisabled('Probe');
    cornerstoneTools.setToolDisabled('Magnify');
    cornerstoneTools.setToolDisabled('Rotate');
    cornerstoneTools.setToolDisabled('Bidirectional');
    cornerstoneTools.setToolDisabled('CobbAngle');
    cornerstoneTools.setToolDisabled('FreehandRoi');
    cornerstoneTools.setToolDisabled('RectangleRoi');
    cornerstoneTools.setToolDisabled('ZoomMouseWheel');
    cornerstoneTools.setToolDisabled('TextMarker');
    cornerstoneTools.setToolDisabled('Brush');
    cornerstoneTools.setToolDisabled('Pan');
    cornerstoneTools.setToolDisabled('ArrowAnnotate');
    cornerstoneTools.setToolDisabled('DragProbe');
    cornerstoneTools.setToolDisabled('StackScrollMouseWheel');
}

document.getElementById('eraser').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活eraser左键
    cornerstoneTools.setToolActive('Eraser',{mouseButtonMask:1})
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ });
})

document.getElementById('pan').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活Pan左键
    cornerstoneTools.setToolActive('Pan', { mouseButtonMask: 1 });
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ });
})

document.getElementById('arrow').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活ArrowAnnotate左键
    cornerstoneTools.setToolActive('ArrowAnnotate', { mouseButtonMask: 1 });
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ });
})

document.getElementById('brush').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活Brush左键
    cornerstoneTools.setToolActive('Brush', { mouseButtonMask: 1 });
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ });
})

document.getElementById('textMarker').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活TextMarkerTool左键
    cornerstoneTools.setToolActive('TextMarker', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ });
})

document.getElementById('wwwc').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活wwwc左键
    cornerstoneTools.setToolActive('Wwwc',{mouseButtonMask:1})
    cornerstoneTools.setToolActive('StackScrollMouseWheel',{ });
})
document.getElementById('angle').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活angle左键
    cornerstoneTools.setToolActive('Angle',{mouseButtonMask:1})
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ });
})

document.getElementById('zoomMouseWheel').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活zoom滚动
    cornerstoneTools.setToolActive('ZoomMouseWheel', { mouseButtonMask: 1 })
})
document.getElementById('length').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活length左键
    cornerstoneTools.setToolActive('Length', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ });
})
document.getElementById('probe').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活Probe左键
    cornerstoneTools.setToolActive('Probe', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ });
})

document.getElementById('dragProbe').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活Probe左键
    cornerstoneTools.setToolActive('DragProbe', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ });
})

document.getElementById('magnify').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活Magnify左键
    cornerstoneTools.setToolActive('Magnify', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('StackScrollMouseWheel',{ })
})
document.getElementById('rotate').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活rotate左键
    cornerstoneTools.setToolActive('Rotate', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('StackScrollMouseWheel',{ })
})
document.getElementById('bidirectional').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活bidirectional左键
    cornerstoneTools.setToolActive('Bidirectional', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ })
})
document.getElementById('cobbangle').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活cobbangle左键
    cornerstoneTools.setToolActive('CobbAngle', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ })
})
document.getElementById('freehanroi').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活freehanroi左键
    cornerstoneTools.setToolActive('FreehandRoi', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ })
})

document.getElementById('rectangleRoi').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活rectangleRoi左键
    cornerstoneTools.setToolActive('RectangleRoi', { mouseButtonMask: 1 })
    cornerstoneTools.setToolActive('ZoomMouseWheel',{ })
})
//滚动查看
document.getElementById('stackScrollMouseWheel').addEventListener('click',function(){
    //使得绑定左键的其他工具失效
    disableAllTools();
    //激活stackScrollMouseWheel左键
    cornerstoneTools.setToolActive('StackScrollMouseWheel',{ })
})