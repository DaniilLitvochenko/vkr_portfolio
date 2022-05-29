program lr8;

var ep, k, u, s, x,m: real;

begin
ep:=0.0001;
k:=1;
u:=1;
s:=1;
x:=0.5;
while abs(u)>ep do
begin
m:=x/k;
u:=m*u;
s:=s+u;
k:=k+1;
end;
writeln(s);
writeln(k);
end.