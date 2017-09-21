function cases
    x=-2; y=-0.4;
    xc=zonesx(x,y);
    yc=zonesy(x,y);
    xc,yc
end

function x=zonesx(x,y)
    x=x-y;
end
function y=zonesy(x,y)
    y=1-(x*y);
end

