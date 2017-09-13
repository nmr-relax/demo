hide
select bb, (name ca,n,c)
show lines, bb
color black, bb
delete bb
bg_color white

set_color pept_colour_39, [0.144504702706, 0.505478601497, 0.894068265746]
select pept_bond, (name ca,n and resi 39) or (name ca,c and resi 38)
as sticks, pept_bond
set_bond stick_radius, 0.84856810593, pept_bond
set_bond stick_color, pept_colour_39, pept_bond
delete pept_bond

set_color pept_colour_40, [0.135302789194, 0.473290234709, 0.900813891587]
select pept_bond, (name ca,n and resi 40) or (name ca,c and resi 39)
as sticks, pept_bond
set_bond stick_radius, 0.921890125948, pept_bond
set_bond stick_color, pept_colour_40, pept_bond
delete pept_bond
