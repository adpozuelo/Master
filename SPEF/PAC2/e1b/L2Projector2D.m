function L2Projector2D(res)
g=[2     2     2     2     2     2     2     2     2     2     2     2;
     1     3     2     0     0     2     2     2     1     1     0     2;
     2     3     1     0     1     3     2     2     1     1     1     3;
     1     0     2     3     0     0     0     2     0     2     3     3;
     1     3     2     0     0     0     1     3     1     3     3     3;
     1     1     1     1     1     1     0     0     1     1     0     0;
     0     0     0     0     0     0     1     1     0     0     1     1];
 [p,e,t] = initmesh(g,'hmax',res);
 M = MassAssembler2D(p,t);
 b = LoadAssembler2D(p,t,@Seno);
 Pf = M\b;
 pdeplot(p,[],t,'XYData',Pf,'XYStyle','interp',...
         'ZData',Pf,'ZStyle','continuous',...
         'ColorMap','jet','Mesh','on'); 