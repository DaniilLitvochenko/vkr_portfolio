program lr5;

procedure pr;
var i:integer;
begin
writeln('|-----|----------|');
writeln('|Дюймы|Сантиметры|');
writeln('|-----|----------|');
for i:=1 to 100 do
begin
writeln('|',i:5,'|',i*2.5:10:1,'|');
end;
writeln('|-----|----------|');
end;

begin 
pr();
end.