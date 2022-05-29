unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, ExtCtrls, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
var
l, n, xsc, ysc : integer;
x, y, a, b : real;
begin
n := StrtoInt(Edit1.Text);
l := StrtoInt(Edit2.Text);

Image1.Canvas.Pen.Color:=clWhite;
Image1.Canvas.Rectangle(0,0,Image1.Width,Image1.Height);
Image1.Canvas.Pen.Color:=clRed;
a:=((360/n)*pi)/180;
x:=Round(Image1.Width/2);
y:=Round(Image1.Height/2);
xsc:=Round(x+l*cos(b));
ysc:=Round(y+l*sin(b));
Image1.Canvas.MoveTo(xsc,ysc);

b:=0;
  while b<360 do
      begin
       xsc:=Round(x+l*cos(b));
       ysc:=Round(y+l*sin(b));
       Image1.Canvas.LineTo(xsc,ysc);
       b:=b+a;
     end;

end;
end.

