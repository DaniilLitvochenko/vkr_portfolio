program mayatnik;

var x, u, m, g, k, v: real;

begin
g:=9.8;
writeln('Введите коэффициент силы трения: ');
readln(u);
writeln('Введите массу тела: ');
readln(m);
writeln('Введите коэффициент жесткости пружины: ');
readln(k);
writeln('Введите скорость: ');
readln(v);
x:=(-u*m*g+sqrt(u*u*m*m*g*g+k*m*v*v))/k;
writeln('Максимальная длина растяжения пружины при введенных данных: ', x);
end.