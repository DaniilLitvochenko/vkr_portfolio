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
const
  n=6;
  l=2;
  M: array[1..n,1..l]of real=((10,10),(10,30),(30,30),(20,25),(30,20),(10,20));
var
   p1, p2, p3 : array[1..l,1..l] of real;
   p : array[1..n,1..l] of real;
   i, j, t, xsc, ysc:integer;
   kx, ky, xmax, ymin, ymax, xmin, a:real;
begin
  xmax:=100;
  ymin:=-100;
  ymax:=100;
  xmin:=-100;
  Image1.Canvas.Rectangle(0, 0, Image1.Width, Image1.Height);
  Image1.Canvas.pen.Color := clblue;
  kx:=Image1.Width/(xmax-xmin);
  ky:=Image1.Height/(ymax-ymin);
  xsc:=Round((0-Xmin)*kx);
  ysc:=Round(Image1.Height-(0-ymin)*ky);
  Image1.Canvas.MoveTo(xsc,0);
  Image1.Canvas.LineTo(xsc,Image1.Height);
  Image1.Canvas.MoveTo(0,ysc);
  Image1.Canvas.LineTo(Image1.Width,ysc);
  Image1.Canvas.Pen.Color:=clblue;
  Image1.canvas.moveto(Round((M[1,1]-Xmin)*kx),Round(Image1.Height-(M[1,2]-ymin)*ky));
  for i:=2 to n do
  Image1.canvas.lineto(Round((M[i,1]-Xmin)*kx),Round(Image1.Height-(M[i,2]-ymin)*ky));
  a:=(StrtoInt(Edit1.Text))*(pi/180);
  p1[1,1]:=cos(a);
  p1[1,2]:=sin(a);
  p1[2,1]:=-sin(a);
  p1[2,2]:=cos(a);
  p2[1,1]:=StrtoInt(Edit2.Text);
  p2[1,2]:=StrtoInt(Edit3.Text);
  p2[2,1]:=StrtoInt(Edit4.Text);
   p2[2,2]:=StrtoInt(Edit5.Text);
  for i:=1 to l do
  for j:=1 to l do
    begin
      p3[i,j]:=0;
     for t:=1 to l do
    p3[i,j]:=p3[i,j]+p1[i,t]*p2[t,j];
   end;
  for i:=1 to n do
  for j:=1 to l do
    begin
      p[i,j]:=0;
      for t:=1 to l do
      p[i,j]:=p[i,j]+M[i,t]*p3[t,j];
   end;
Image1.Canvas.pen.Color := clwhite;
Image1.Canvas.Rectangle(0, 0, Image1.Width, Image1.Height);
Image1.Canvas.pen.Color := clblue;
Image1.Canvas.MoveTo(xsc,0);
Image1.Canvas.LineTo(xsc,Image1.Height);
Image1.Canvas.MoveTo(0,ysc);
Image1.Canvas.LineTo(Image1.Width,ysc);
Image1.canvas.MoveTo(Round((p[1,1]-Xmin)*kx),Round(Image1.Height-(p[1,2]-ymin)*ky));
for i:=2 to n do
Image1.canvas.LineTo(Round((p[i,1]-Xmin)*kx),Round(Image1.Height-(p[i,2]-ymin)*ky));
end;
end.

