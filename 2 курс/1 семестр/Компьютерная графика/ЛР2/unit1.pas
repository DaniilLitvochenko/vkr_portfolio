unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ExtCtrls;

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
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
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
var x1, y1, x2, y2, x3, y3: integer;
begin
  x1:=StrToInt(Edit1.Text);
  y1:=StrToInt(Edit2.Text);
  x2:=StrToInt(Edit3.Text);
  y2:=StrToInt(Edit4.Text);
  x3:=StrToInt(Edit5.Text);
  y3:=StrToInt(Edit6.Text);

  Image1.Canvas.pen.Color := clWhite;
  Image1.Canvas.Line(x1,y1,x2,y2);
  Image1.Canvas.pen.Color := clRed;
  Image1.Canvas.Line(x2,y2,x3,y3);
  Image1.Canvas.pen.Color := clBlue;
  Image1.Canvas.Line(x1,y1,x3,y3);
end;

end.

