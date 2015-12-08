LoadPlugin("D:\GreenSoftware\小丸工具箱rev190\tools\avsfilter\VSFilter.DLL")
LoadPlugin("D:\GreenSoftware\小丸工具箱rev190\tools\avsfilter\LSMASHSource.DLL")
LWLibavVideoSource("C:\Users\dcc\Desktop\bandicam 2015-10-27 09-58-31-927_1.mp4")
ConvertToYV12()
LanczosResize(1280,720)
convertfps=true
ChangeFPS(15)