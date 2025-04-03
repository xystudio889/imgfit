import argparse
import img_fit

class SharedAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        # 调用共享方法
        self.handle_output(parser, namespace, values)

    @staticmethod
    def handle_output(parser, namespace, values):
        # 共享的处理逻辑
        setattr(namespace, "output", values) 

parser = argparse.ArgumentParser(description="imgfit commands")
subparsers = parser.add_subparsers(dest="command", required=True)

p_text = subparsers.add_parser("text", help="Get the image text")
p_text.add_argument("from_img", nargs=None, help="The image you want to change") 
p_text.add_argument("chars", nargs="+", help="The chars ypu want to make a text painting.") 
p_text.add_argument("-o","--output",nargs="?", action=SharedAction, type=str,help="the output path.")  
p_fitter = subparsers.add_parser("fitter", help="Fitter the image.")
p_fitter.add_argument("from_img",nargs=None,help="The image you want to change")
p_fitter.add_argument("fitter_img",nargs=None,help="The fitter image.")
p_fitter.add_argument("output_img",nargs=None,help="The output image path.")

args = parser.parse_args()
try:
    if args.command == "text":
        print(args)
        img_fit.text_painting(args.from_img,args.chars,args.output)
    elif args.command == "fitter":
        img_fit.add_fitter(args.from_img,args.fitter_img,args.output_img)
except FileNotFoundError as fe:
    print("Error:",fe)
else:
    print("fit image successfull!")