program lr5;

var n: integer;

function fib(n:integer):integer;
var
    a,b,c,i: integer;
begin
    write('n = ');
    a := 0;
    b := 1;
    c := 0;
    for i:=2 to n+1 do 
    begin
        write(a+b,' ');
        c := b;
        b := a + b;
        a := c;   
  end;
end;

begin
readln(n);
fib(n);
end.