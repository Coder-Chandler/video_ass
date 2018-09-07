from ffmpy import FFmpeg

def edition(filename):
    ff = FFmpeg(
        inputs={filename: None},
        outputs={'output.mp4': '-r 5 -b:v 50K'}
    )
    return ff.run()