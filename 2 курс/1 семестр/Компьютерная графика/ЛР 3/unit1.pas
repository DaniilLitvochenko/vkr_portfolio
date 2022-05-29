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
    Edit4: TEdit;
    Edit5: TEdit;
    Edit6: TEdit;
    Edit7: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
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
   xmin, ymin, xmax, ymax, hg, w, n, xsc, ysc : integer;
   a, b, c, h, x, y, kx, ky : real;
begin
   hg:=image1.Height;
   w:=image1.Width;
   xmin:=StrtoInt(Edit4.Text);
   ymin:=StrtoInt(Edit5.Text);
   xmax:=StrtoInt(Edit6.Text);
   ymax:=StrtoInt(Edit7.Text);

   a:=StrtoInt(Edit1.Text);
   b:=StrtoInt(Edit2.Text);
   c:=StrtoInt(Edit3.Text);
   n:=77;
   h:=w/n;
   kx:=w/(xmax-xmin);
   ky:=hg/(ymax-ymin);

   image1.Canvas.Rectangle(0,0,w,hg);
   image1.Canvas.MoveTo(0,round(ymax*ky));
   image1.Canvas.LineTo(w,round(ymax*ky));
   image1.Canvas.MoveTo(round(-xmin*kx),0);
   image1.Canvas.LineTo(round(-xmin*kx),hg);

   x:=xmin;
   image1.Canvas.MoveTo(xmin, round(a*x*x+b*x+c));
 while x<=xmax do
   begin
   y:=a*x*x+b*x+c;
   xsc:=round((x-xmin)*kx);
   ysc:=round(hg-(y-ymin)*ky);
   image1.Canvas.LineTo(xsc,ysc);
   x:=x+h;
   end;
 end;
end.

