unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Edit4: TEdit;
    Edit5: TEdit;
    Edit6: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    procedure Label1Click(Sender: TObject);
    procedure Label2Click(Sender: TObject);
    procedure Label3Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Label1Click(Sender: TObject);
begin
 Edit1.Text:= '0.0.255'
end;

procedure TForm1.Label2Click(Sender: TObject);
begin
 Edit2.Text:= '0.0.0';
end;

procedure TForm1.Label3Click(Sender: TObject);
begin
  Edit3.Text:= '255.0.0';
end;



procedure TForm1.Label5Click(Sender: TObject);
begin
  Edit5.Text:= '255.255.0';
end;

procedure TForm1.Label6Click(Sender: TObject);
begin
  Edit6.Text:= '0.128.128';
end;
end.

