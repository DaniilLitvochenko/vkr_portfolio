program lr8;

var uv, uvh, r, c, ep, t, h,e: real;

begin
r:=2;
c:=0.01;
uvh:=50;
t:=0.01;
h:=0.01;
ep:=0.001;
while abs(uvh-uv)>=ep do
begin
uv:=uvh*(1-exp(-t/(r*c)));
t:=t+h;
end;
writeln(uv);
end.