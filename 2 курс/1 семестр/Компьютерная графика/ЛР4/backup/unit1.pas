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
    Edit3: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
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
const
  g=9.8;
var
  u0, a, kx, ky,tmax, t, x, y, dt : real;
  xsc, ysc, n : integer;
begin
  u0:=StrtoInt(Edit1.Text);
  n:=StrtoInt(Edit2.Text);
  a:=StrtoInt(Edit3.Text);

 Image1.Canvas.Rectangle(0,0,Image1.Width,Image1.Height);
 Image1.Canvas.pen.Color := clblue;
 a:=a*pi/180;
 kx:=Image1.Width/((u0*u0)/g);
 ky:=Image1.Height/((u0*u0)/(2*g));
 tmax:=(2*u0*sin(a))/g;
 t:=0;
 dt:=tmax/n;

 while t<=tmax do
  begin
  x:=u0*cos(a)*t;
  y:=u0*sin(a)*t-g*t*t/2;
  xsc:=round(x*kx);
  ysc:=round(Image1.Height-y*ky);
  Image1.Canvas.Ellipse(xsc,ysc,xsc+4,ysc+4);
  t:=t+dt;
 end;
end;
end.

