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
   xmin, ymin, xmax, ymax, h, w, n, Xsc, Ysc : integer;
   A, B, C, shag, x, y, Kx, Ky : real;
begin
   h:=image1.Height;
   w:=image1.Width;
   xmin:=StrtoInt(Edit4.Text);
   ymin:=StrtoInt(Edit5.Text);
   xmax:=StrtoInt(Edit6.Text);
   ymax:=StrtoInt(Edit7.Text);

   A:=StrtoInt(Edit1.Text);
   B:=StrtoInt(Edit2.Text);
   C:=StrtoInt(Edit3.Text);
   n:=77;
   shag:=w/n;
   Kx:=w/(xmax-xmin);
   Ky:=h/(ymax-ymin);

   image1.Canvas.Rectangle(0,0,w,h);
   image1.Canvas.MoveTo(0,round(ymax*Ky));
   image1.Canvas.LineTo(w,round(ymax*Ky));
   image1.Canvas.MoveTo(round(-xmin*Kx),0);
   image1.Canvas.LineTo(round(-xmin*Kx),h);

   x:=xmin;
   image1.Canvas.MoveTo(xmin, round(A*x*x+B*x+C));
 while x<=xmax do
   begin
   y:=A*x*x+B*x+C;
   Xsc:=round((x-xmin)*Kx);
   Ysc:=round(h-(y-ymin)*Ky);
   image1.Canvas.LineTo(Xsc,Ysc);
   x:=x+shag;
   end;
 end;
end.

