program lr4;

var y: real;

function fnfact(n: integer):real;
var i:integer;
    rez: real;
begin
rez:=1;
for i:=2 to n do
  rez:=rez*i;
fnfact:=rez;
end;

function fnsum(x,n:integer):real;
var rez: real;
    i: integer;
begin
rez:=0;
for i:=1 to n do
  begin
    rez:=rez+((1/fnfact(i+1))*((exp(ln(x)*(2*i+1))/(2*i+1))));
  end;
rez:=rez/(5.5+x*x+fnfact(3*n));
fnsum:=rez;
end;

begin
y:=fnsum(1,5);
writeln(y);
end.

