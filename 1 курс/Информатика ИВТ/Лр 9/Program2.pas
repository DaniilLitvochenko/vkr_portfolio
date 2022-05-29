program lr9;

var a, o, h, d,sina,cosa,chet: real;

begin
h:=0.1;
d:=30*0.017;
o:=45*0.017;
a:=arcsin(cos(o)*(sin(h)/sin(d)));
sina:=(cos(o)*sin(h))/sin(d);
cosa:=(sin(o)-sin(o)*cos(d))/(cos(o)*sin(d));
if (sina>0) and (cosa>0) then begin a:=abs(a); chet:=1; end;
if (sina>0) and (cosa<0) then begin a:=pi-abs(a); chet:=2; end;
if (sina<0) and (cosa<0) then begin a:=pi+abs(a); chet:=3; end;
if (sina<0) and (cosa>0) then begin a:=2*pi-abs(a); chet:=4; end;
writeln('Угол равен: ',a*57.2958);
writeln('Четверть: ',chet);
end.