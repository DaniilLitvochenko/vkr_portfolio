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
    Image1: TImage;
    Label1: TLabel;
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
const n=4; l=4;
var
  xmax, xmin, ymin, ymax, xs, ys, a, i, j, t: real;
  p: array [] of real;
  p1: array [] of real;
  p2: array [] of real;
  p3: array [] of real;
begin
  xmax := 150;
  ymin := -150;
  ymax := 150;
  xmin := -150;
  xs := Round(-xmin);
  ys := Round(Image1.Height - (-ymin));

  a := (StrToInt(Edit1.Text)) * (pi / 180);

  p2[1, 1] := cos(a);
  p2[1, 2] := sin(a);
  p2[2, 1] := -sin(a);
  p2[2, 2] := cos(a);

  for i := 1 to l do
    for j := 1 to l do
    begin
      p3[i, j] := 0;
      for t := 1 to l do
        p3[i, j] := p3[i, j] + p1[i, t] * p2[t, j];
    end;
  for i := 1 to n do
    for j := 1 to l do
    begin
      p[i, j] := 0;
      for t := 1 to l do
        p[i, j] := p[i, j] + M[i, t] * p3[t, j];
    end;

  for i := 1 to n do
  begin
    scr[i, 1] := round(M[i, 1] + Image1.Width / 2);
    scr[i, 2] := round(Image1.Width / 2 - M[i, 2]);
  end;
  Image1.Canvas.pen.Color := clWhite;
  Image1.Canvas.Rectangle(0, 0, Image1.Width, Image1.Height);
  Image1.Canvas.pen.Color := clBlue;
  Image1.Canvas.MoveTo(xs, 0);
  Image1.Canvas.LineTo(xs, Image1.Height);
  Image1.Canvas.MoveTo(0, ys);
  Image1.Canvas.LineTo(Image1.Width, ys);

  Image1.canvas.MoveTo(scr[1, 1], scr[1, 2]);
  for i := 2 to n do
    Image1.canvas.lineto(scr[i, 1], scr[i, 2]);
  for i := 1 to n do
  begin
    scr[i, 1] := round(p[i, 1] + Image1.Width / 2);
    scr[i, 2] := round(Image1.Width / 2 - p[i, 2]);
  end;
  Image1.canvas.MoveTo(scr[1, 1], scr[1, 2]);
  for i := 2 to n do
    Image1.canvas.lineto(scr[i, 1], scr[i, 2]);
end;


end.
