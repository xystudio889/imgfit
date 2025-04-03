import argparse
import img_fit

class TextAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        self.handle_output(parser, namespace, values)

    @staticmethod
    def handle_output(parser, namespace, values):
        setattr(namespace, "output", values) 

class VersionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        self.handle_output(parser, namespace, values)

    @staticmethod
    def handle_output(parser, namespace, values):
        setattr(namespace, "v", values) 

parser = argparse.ArgumentParser(description="imgfit commands")
subparsers = parser.add_subparsers(dest="command", required=False)

p_text = subparsers.add_parser("text", help="Get the image text")
p_text.add_argument("from_img", help="The image you want to change") 
p_text.add_argument("chars", nargs="+", help="The chars ypu want to make a text painting.") 
p_text.add_argument("-o","--output",nargs="?", type=str,help="The output path.")  

p_fitter = subparsers.add_parser("fitter", help="Fitter the image.")
p_fitter.add_argument("from_img",help="The image you want to change")
p_fitter.add_argument("fitter_img",help="The fitter image.")
p_fitter.add_argument("output_img",help="The output image path.")

parser.add_argument("-v","--version",nargs="?",action=VersionAction,type=str,help="get the imgfit version.")

args = parser.parse_args()
try:
    if args.command == "text":
        img_fit.text_painting(args.from_img,args.chars,args.output)
    elif args.command == "fitter":
        img_fit.add_fitter(args.from_img,args.fitter_img,args.output_img)
    elif args.v is None:
        pass
except FileNotFoundError as fe:
    print("Error:",fe)
except AttributeError:
    print("Version : imgfit",img_fit.__version__)
else:
    print("fit image successfull!")