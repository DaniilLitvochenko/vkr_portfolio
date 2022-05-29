program lr9;

var 
  A:array[1..5] of integer;
  i,enter:integer;

begin
writeln('Введите пятизначное число: ');
readln(enter);
for i:=1 to 5 do
  begin
  A[i]:=enter mod 10;
  enter:=enter div 10;
  end;
if (A[1]=A[5]) and (A[2]=A[4]) then 
  writeln('Число является палиндромом')
else writeln('Не является палиндромом')
end.