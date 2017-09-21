function M=MassAssembler2D(p,t)
np = size(p,2);
nt = size(t,2);
M = sparse(np,np);
for K=1:nt
    loc2glb = t(1:3,K);
    x=p(1,loc2glb);
    y=p(2,loc2glb);
    area = polyarea(x,y);
    MK = [2 1 1;
          1 2 1;
          1 1 2]/12*area;
      M(loc2glb,loc2glb) = M(loc2glb,loc2glb)+MK;
end