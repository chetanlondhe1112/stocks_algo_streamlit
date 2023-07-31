from streamlit_lottie import st_lottie
import json

class statics:

    def __init__(self):
        pass
        
    def lottie_files(self,file_path=str):
        with open(file=file_path,mode="r") as f:
            return json.load(f)

    def lottie_select(self,file_path=str,quality=str,height=int):
        """
            Reads the json lottiee animations 
            -file_path=str|path of the file
            -height=int|height of image, width paramter is not available
            -quality=str|"low","high"
        """
        lottie_intro=self.lottie_files(file_path=file_path)
        return st_lottie(animation_source=lottie_intro,speed=1,reverse=False,loop=True,quality=quality,height=height,)