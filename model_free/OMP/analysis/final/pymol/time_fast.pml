hide
select bb, (name ca,n,c)
show lines, bb
color black, bb
delete bb
bg_color white

set_color pept_colour_9, [1, 1, 1]
select pept_bond, (name ca,n and resi 9) or (name ca,c and resi 8)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_9, pept_bond
delete pept_bond

set_color pept_colour_10, [1, 1, 1]
select pept_bond, (name ca,n and resi 10) or (name ca,c and resi 9)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_10, pept_bond
delete pept_bond

set_color pept_colour_11, [0.218164014635, 0.763139461552, 0.840071001224]
select pept_bond, (name ca,n and resi 11) or (name ca,c and resi 10)
as sticks, pept_bond
set_bond stick_radius, 0.261641317648, pept_bond
set_bond stick_color, pept_colour_11, pept_bond
delete pept_bond

set_color pept_colour_12, [1, 1, 1]
select pept_bond, (name ca,n and resi 12) or (name ca,c and resi 11)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_12, pept_bond
delete pept_bond

set_color pept_colour_13, [0.216520321994, 0.757389811598, 0.841275939255]
select pept_bond, (name ca,n and resi 13) or (name ca,c and resi 12)
as sticks, pept_bond
set_bond stick_radius, 0.274738470163, pept_bond
set_bond stick_color, pept_colour_13, pept_bond
delete pept_bond

set_color pept_colour_15, [1, 1, 1]
select pept_bond, (name ca,n and resi 15) or (name ca,c and resi 14)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_15, pept_bond
delete pept_bond

set_color pept_colour_16, [0.210276316723, 0.735548231406, 0.84585321802]
select pept_bond, (name ca,n and resi 16) or (name ca,c and resi 15)
as sticks, pept_bond
set_bond stick_radius, 0.324491500215, pept_bond
set_bond stick_color, pept_colour_16, pept_bond
delete pept_bond

set_color pept_colour_17, [0.207729583898, 0.726639739692, 0.847720145668]
select pept_bond, (name ca,n and resi 17) or (name ca,c and resi 16)
as sticks, pept_bond
set_bond stick_radius, 0.344784192045, pept_bond
set_bond stick_color, pept_colour_17, pept_bond
delete pept_bond

set_color pept_colour_18, [0.209240428672, 0.731924686749, 0.846612594121]
select pept_bond, (name ca,n and resi 18) or (name ca,c and resi 17)
as sticks, pept_bond
set_bond stick_radius, 0.332745588272, pept_bond
set_bond stick_color, pept_colour_18, pept_bond
delete pept_bond

set_color pept_colour_19, [1, 1, 1]
select pept_bond, (name ca,n and resi 19) or (name ca,c and resi 18)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_19, pept_bond
delete pept_bond

set_color pept_colour_20, [0.177338087296, 0.620330042414, 0.869999171066]
select pept_bond, (name ca,n and resi 20) or (name ca,c and resi 19)
as sticks, pept_bond
set_bond stick_radius, 0.586947511587, pept_bond
set_bond stick_color, pept_colour_20, pept_bond
delete pept_bond

set_color pept_colour_21, [0.18655933148, 0.652586028046, 0.863239374533]
select pept_bond, (name ca,n and resi 21) or (name ca,c and resi 20)
as sticks, pept_bond
set_bond stick_radius, 0.513471462311, pept_bond
set_bond stick_color, pept_colour_21, pept_bond
delete pept_bond

set_color pept_colour_22, [0.194125247486, 0.67905166252, 0.857693045668]
select pept_bond, (name ca,n and resi 22) or (name ca,c and resi 21)
as sticks, pept_bond
set_bond stick_radius, 0.453185278998, pept_bond
set_bond stick_color, pept_colour_22, pept_bond
delete pept_bond

set_color pept_colour_23, [1, 1, 1]
select pept_bond, (name ca,n and resi 23) or (name ca,c and resi 22)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_23, pept_bond
delete pept_bond

set_color pept_colour_24, [1, 1, 1]
select pept_bond, (name ca,n and resi 24) or (name ca,c and resi 23)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_24, pept_bond
delete pept_bond

set_color pept_colour_25, [0.20035718497, 0.700851029496, 0.853124613408]
select pept_bond, (name ca,n and resi 25) or (name ca,c and resi 24)
as sticks, pept_bond
set_bond stick_radius, 0.403528406614, pept_bond
set_bond stick_color, pept_colour_25, pept_bond
delete pept_bond

set_color pept_colour_26, [1, 1, 1]
select pept_bond, (name ca,n and resi 26) or (name ca,c and resi 25)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_26, pept_bond
delete pept_bond

set_color pept_colour_27, [1, 1, 1]
select pept_bond, (name ca,n and resi 27) or (name ca,c and resi 26)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_27, pept_bond
delete pept_bond

set_color pept_colour_28, [0.203469457611, 0.711737783994, 0.850843106771]
select pept_bond, (name ca,n and resi 28) or (name ca,c and resi 27)
as sticks, pept_bond
set_bond stick_radius, 0.378729421426, pept_bond
set_bond stick_color, pept_colour_28, pept_bond
delete pept_bond

set_color pept_colour_29, [1, 1, 1]
select pept_bond, (name ca,n and resi 29) or (name ca,c and resi 28)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_29, pept_bond
delete pept_bond

set_color pept_colour_30, [0.197739258077, 0.691693500364, 0.855043731131]
select pept_bond, (name ca,n and resi 30) or (name ca,c and resi 29)
as sticks, pept_bond
set_bond stick_radius, 0.424388381858, pept_bond
set_bond stick_color, pept_colour_30, pept_bond
delete pept_bond

set_color pept_colour_31, [0.194628514476, 0.680812094462, 0.857324116878]
select pept_bond, (name ca,n and resi 31) or (name ca,c and resi 30)
as sticks, pept_bond
set_bond stick_radius, 0.449175183458, pept_bond
set_bond stick_color, pept_colour_31, pept_bond
delete pept_bond

set_color pept_colour_32, [1, 1, 1]
select pept_bond, (name ca,n and resi 32) or (name ca,c and resi 31)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_32, pept_bond
delete pept_bond

set_color pept_colour_33, [0.209204866813, 0.731800291084, 0.846638663372]
select pept_bond, (name ca,n and resi 33) or (name ca,c and resi 32)
as sticks, pept_bond
set_bond stick_radius, 0.333028949694, pept_bond
set_bond stick_color, pept_colour_33, pept_bond
delete pept_bond

set_color pept_colour_35, [0.147612288126, 0.516348960057, 0.891790195159]
select pept_bond, (name ca,n and resi 35) or (name ca,c and resi 34)
as sticks, pept_bond
set_bond stick_radius, 0.823806469118, pept_bond
set_bond stick_color, pept_colour_35, pept_bond
delete pept_bond

set_color pept_colour_36, [1, 1, 1]
select pept_bond, (name ca,n and resi 36) or (name ca,c and resi 35)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_36, pept_bond
delete pept_bond

set_color pept_colour_37, [1, 1, 1]
select pept_bond, (name ca,n and resi 37) or (name ca,c and resi 36)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_37, pept_bond
delete pept_bond

set_color pept_colour_38, [1, 1, 1]
select pept_bond, (name ca,n and resi 38) or (name ca,c and resi 37)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_38, pept_bond
delete pept_bond

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

set_color pept_colour_41, [1, 1, 1]
select pept_bond, (name ca,n and resi 41) or (name ca,c and resi 40)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_41, pept_bond
delete pept_bond

set_color pept_colour_43, [0.138006309419, 0.48274717, 0.898832028155]
select pept_bond, (name ca,n and resi 43) or (name ca,c and resi 42)
as sticks, pept_bond
set_bond stick_radius, 0.900348132119, pept_bond
set_bond stick_color, pept_colour_43, pept_bond
delete pept_bond

set_color pept_colour_44, [0.184366238232, 0.644914570388, 0.86484706042]
select pept_bond, (name ca,n and resi 44) or (name ca,c and resi 43)
as sticks, pept_bond
set_bond stick_radius, 0.530946308912, pept_bond
set_bond stick_color, pept_colour_44, pept_bond
delete pept_bond

set_color pept_colour_45, [1, 1, 1]
select pept_bond, (name ca,n and resi 45) or (name ca,c and resi 44)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_45, pept_bond
delete pept_bond

set_color pept_colour_46, [0.200083232897, 0.699892742962, 0.853325438833]
select pept_bond, (name ca,n and resi 46) or (name ca,c and resi 45)
as sticks, pept_bond
set_bond stick_radius, 0.405711291658, pept_bond
set_bond stick_color, pept_colour_46, pept_bond
delete pept_bond

set_color pept_colour_47, [1, 1, 1]
select pept_bond, (name ca,n and resi 47) or (name ca,c and resi 46)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_47, pept_bond
delete pept_bond

set_color pept_colour_49, [0.209583864925, 0.733126029498, 0.846360832087]
select pept_bond, (name ca,n and resi 49) or (name ca,c and resi 48)
as sticks, pept_bond
set_bond stick_radius, 0.330009044424, pept_bond
set_bond stick_color, pept_colour_49, pept_bond
delete pept_bond

set_color pept_colour_50, [1, 1, 1]
select pept_bond, (name ca,n and resi 50) or (name ca,c and resi 49)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_50, pept_bond
delete pept_bond

set_color pept_colour_51, [0.217322181986, 0.760194724239, 0.840688121572]
select pept_bond, (name ca,n and resi 51) or (name ca,c and resi 50)
as sticks, pept_bond
set_bond stick_radius, 0.268349147519, pept_bond
set_bond stick_color, pept_colour_51, pept_bond
delete pept_bond

set_color pept_colour_53, [0.213972059538, 0.74847596922, 0.843143988227]
select pept_bond, (name ca,n and resi 53) or (name ca,c and resi 52)
as sticks, pept_bond
set_bond stick_radius, 0.295043350297, pept_bond
set_bond stick_color, pept_colour_53, pept_bond
delete pept_bond

set_color pept_colour_54, [1, 1, 1]
select pept_bond, (name ca,n and resi 54) or (name ca,c and resi 53)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_54, pept_bond
delete pept_bond

set_color pept_colour_55, [1, 1, 1]
select pept_bond, (name ca,n and resi 55) or (name ca,c and resi 54)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_55, pept_bond
delete pept_bond

set_color pept_colour_56, [0.225946971949, 0.790364308251, 0.83436556638]
select pept_bond, (name ca,n and resi 56) or (name ca,c and resi 55)
as sticks, pept_bond
set_bond stick_radius, 0.199625721524, pept_bond
set_bond stick_color, pept_colour_56, pept_bond
delete pept_bond

set_color pept_colour_57, [1, 1, 1]
select pept_bond, (name ca,n and resi 57) or (name ca,c and resi 56)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_57, pept_bond
delete pept_bond

set_color pept_colour_58, [0.183944650488, 0.6434398531, 0.86515611279]
select pept_bond, (name ca,n and resi 58) or (name ca,c and resi 57)
as sticks, pept_bond
set_bond stick_radius, 0.534305573804, pept_bond
set_bond stick_color, pept_colour_58, pept_bond
delete pept_bond

set_color pept_colour_59, [0.101174740851, 0.35391004967, 0.925832062484]
select pept_bond, (name ca,n and resi 59) or (name ca,c and resi 58)
as sticks, pept_bond
set_bond stick_radius, 1.19382676613, pept_bond
set_bond stick_color, pept_colour_59, pept_bond
delete pept_bond

set_color pept_colour_60, [0.124332992704, 0.434917799179, 0.908855495389]
select pept_bond, (name ca,n and resi 60) or (name ca,c and resi 59)
as sticks, pept_bond
set_bond stick_radius, 1.00929886292, pept_bond
set_bond stick_color, pept_colour_60, pept_bond
delete pept_bond

set_color pept_colour_62, [0.153234015888, 0.536013808564, 0.887669087955]
select pept_bond, (name ca,n and resi 62) or (name ca,c and resi 61)
as sticks, pept_bond
set_bond stick_radius, 0.779011825594, pept_bond
set_bond stick_color, pept_colour_62, pept_bond
delete pept_bond

set_color pept_colour_63, [0.170474571609, 0.596321409852, 0.875030592924]
select pept_bond, (name ca,n and resi 63) or (name ca,c and resi 62)
as sticks, pept_bond
set_bond stick_radius, 0.641636879609, pept_bond
set_bond stick_color, pept_colour_63, pept_bond
delete pept_bond

set_color pept_colour_64, [0.202580524723, 0.708628289668, 0.851494754785]
select pept_bond, (name ca,n and resi 64) or (name ca,c and resi 63)
as sticks, pept_bond
set_bond stick_radius, 0.38581255201, pept_bond
set_bond stick_color, pept_colour_64, pept_bond
delete pept_bond

set_color pept_colour_65, [0.128490063549, 0.449459266119, 0.905808080904]
select pept_bond, (name ca,n and resi 65) or (name ca,c and resi 64)
as sticks, pept_bond
set_bond stick_radius, 0.97617479244, pept_bond
set_bond stick_color, pept_colour_65, pept_bond
delete pept_bond

set_color pept_colour_66, [0.146262338049, 0.511626823933, 0.892779799996]
select pept_bond, (name ca,n and resi 66) or (name ca,c and resi 65)
as sticks, pept_bond
set_bond stick_radius, 0.834563043434, pept_bond
set_bond stick_color, pept_colour_66, pept_bond
delete pept_bond

set_color pept_colour_67, [0.162420777171, 0.568149172732, 0.880934569724]
select pept_bond, (name ca,n and resi 67) or (name ca,c and resi 66)
as sticks, pept_bond
set_bond stick_radius, 0.705810540473, pept_bond
set_bond stick_color, pept_colour_67, pept_bond
delete pept_bond

set_color pept_colour_68, [0.205656933696, 0.719389592771, 0.849239538645]
select pept_bond, (name ca,n and resi 68) or (name ca,c and resi 67)
as sticks, pept_bond
set_bond stick_radius, 0.361299333097, pept_bond
set_bond stick_color, pept_colour_68, pept_bond
delete pept_bond

set_color pept_colour_69, [0.205079887754, 0.717371081465, 0.849662552404]
select pept_bond, (name ca,n and resi 69) or (name ca,c and resi 68)
as sticks, pept_bond
set_bond stick_radius, 0.365897308735, pept_bond
set_bond stick_color, pept_colour_69, pept_bond
delete pept_bond

set_color pept_colour_70, [0.22548159351, 0.788736410766, 0.834706720295]
select pept_bond, (name ca,n and resi 70) or (name ca,c and resi 69)
as sticks, pept_bond
set_bond stick_radius, 0.203333916251, pept_bond
set_bond stick_color, pept_colour_70, pept_bond
delete pept_bond

set_color pept_colour_71, [0.21859672076, 0.764653071024, 0.839753798327]
select pept_bond, (name ca,n and resi 71) or (name ca,c and resi 70)
as sticks, pept_bond
set_bond stick_radius, 0.258193460081, pept_bond
set_bond stick_color, pept_colour_71, pept_bond
delete pept_bond

set_color pept_colour_72, [1, 1, 1]
select pept_bond, (name ca,n and resi 72) or (name ca,c and resi 71)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_72, pept_bond
delete pept_bond

set_color pept_colour_73, [0.222350789028, 0.777784831738, 0.837001812028]
select pept_bond, (name ca,n and resi 73) or (name ca,c and resi 72)
as sticks, pept_bond
set_bond stick_radius, 0.228280565516, pept_bond
set_bond stick_color, pept_colour_73, pept_bond
delete pept_bond

set_color pept_colour_74, [1, 1, 1]
select pept_bond, (name ca,n and resi 74) or (name ca,c and resi 73)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_74, pept_bond
delete pept_bond

set_color pept_colour_76, [1, 1, 1]
select pept_bond, (name ca,n and resi 76) or (name ca,c and resi 75)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_76, pept_bond
delete pept_bond

set_color pept_colour_77, [1, 1, 1]
select pept_bond, (name ca,n and resi 77) or (name ca,c and resi 76)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_77, pept_bond
delete pept_bond

set_color pept_colour_78, [1, 1, 1]
select pept_bond, (name ca,n and resi 78) or (name ca,c and resi 77)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_78, pept_bond
delete pept_bond

set_color pept_colour_79, [0.211590209203, 0.740144237769, 0.844890045843]
select pept_bond, (name ca,n and resi 79) or (name ca,c and resi 78)
as sticks, pept_bond
set_bond stick_radius, 0.314022237429, pept_bond
set_bond stick_color, pept_colour_79, pept_bond
delete pept_bond

set_color pept_colour_80, [0.220622283358, 0.771738505131, 0.838268923754]
select pept_bond, (name ca,n and resi 80) or (name ca,c and resi 79)
as sticks, pept_bond
set_bond stick_radius, 0.242053519063, pept_bond
set_bond stick_color, pept_colour_80, pept_bond
delete pept_bond

set_color pept_colour_81, [1, 1, 1]
select pept_bond, (name ca,n and resi 81) or (name ca,c and resi 80)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_81, pept_bond
delete pept_bond

set_color pept_colour_82, [0.208398184079, 0.728978508451, 0.847230016452]
select pept_bond, (name ca,n and resi 82) or (name ca,c and resi 81)
as sticks, pept_bond
set_bond stick_radius, 0.339456700566, pept_bond
set_bond stick_color, pept_colour_82, pept_bond
delete pept_bond

set_color pept_colour_83, [1, 1, 1]
select pept_bond, (name ca,n and resi 83) or (name ca,c and resi 82)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_83, pept_bond
delete pept_bond

set_color pept_colour_84, [0.19106784007, 0.668356827018, 0.859934332379]
select pept_bond, (name ca,n and resi 84) or (name ca,c and resi 83)
as sticks, pept_bond
set_bond stick_radius, 0.477547091075, pept_bond
set_bond stick_color, pept_colour_84, pept_bond
delete pept_bond

set_color pept_colour_86, [0.203323830851, 0.711228380428, 0.850949861049]
select pept_bond, (name ca,n and resi 86) or (name ca,c and resi 85)
as sticks, pept_bond
set_bond stick_radius, 0.379889794014, pept_bond
set_bond stick_color, pept_colour_86, pept_bond
delete pept_bond

set_color pept_colour_87, [0.204755374243, 0.716235930619, 0.849900442786]
select pept_bond, (name ca,n and resi 87) or (name ca,c and resi 86)
as sticks, pept_bond
set_bond stick_radius, 0.368483073762, pept_bond
set_bond stick_color, pept_colour_87, pept_bond
delete pept_bond

set_color pept_colour_90, [0.131695713339, 0.460672654626, 0.903458122493]
select pept_bond, (name ca,n and resi 90) or (name ca,c and resi 89)
as sticks, pept_bond
set_bond stick_radius, 0.950631766227, pept_bond
set_bond stick_color, pept_colour_90, pept_bond
delete pept_bond

set_color pept_colour_91, [0.174305453813, 0.609721866327, 0.872222296806]
select pept_bond, (name ca,n and resi 91) or (name ca,c and resi 90)
as sticks, pept_bond
set_bond stick_radius, 0.611111921807, pept_bond
set_bond stick_color, pept_colour_91, pept_bond
delete pept_bond

set_color pept_colour_92, [1, 1, 1]
select pept_bond, (name ca,n and resi 92) or (name ca,c and resi 91)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_92, pept_bond
delete pept_bond

set_color pept_colour_94, [0.190960322262, 0.667980728868, 0.860013150214]
select pept_bond, (name ca,n and resi 94) or (name ca,c and resi 93)
as sticks, pept_bond
set_bond stick_radius, 0.478403806678, pept_bond
set_bond stick_color, pept_colour_94, pept_bond
delete pept_bond

set_color pept_colour_95, [0.162154343303, 0.567217184942, 0.881129883793]
select pept_bond, (name ca,n and resi 95) or (name ca,c and resi 94)
as sticks, pept_bond
set_bond stick_radius, 0.707933519495, pept_bond
set_bond stick_color, pept_colour_95, pept_bond
delete pept_bond

set_color pept_colour_96, [0.199747153284, 0.698717133798, 0.853571807951]
select pept_bond, (name ca,n and resi 96) or (name ca,c and resi 95)
as sticks, pept_bond
set_bond stick_radius, 0.408389216861, pept_bond
set_bond stick_color, pept_colour_96, pept_bond
delete pept_bond

set_color pept_colour_97, [1, 1, 1]
select pept_bond, (name ca,n and resi 97) or (name ca,c and resi 96)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_97, pept_bond
delete pept_bond

set_color pept_colour_98, [0.186681886018, 0.653014724798, 0.863149533755]
select pept_bond, (name ca,n and resi 98) or (name ca,c and resi 97)
as sticks, pept_bond
set_bond stick_radius, 0.512494932124, pept_bond
set_bond stick_color, pept_colour_98, pept_bond
delete pept_bond

set_color pept_colour_99, [0.200429187333, 0.701102894335, 0.8530718308]
select pept_bond, (name ca,n and resi 99) or (name ca,c and resi 98)
as sticks, pept_bond
set_bond stick_radius, 0.402954682609, pept_bond
set_bond stick_color, pept_colour_99, pept_bond
delete pept_bond

set_color pept_colour_100, [1, 1, 1]
select pept_bond, (name ca,n and resi 100) or (name ca,c and resi 99)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_100, pept_bond
delete pept_bond

set_color pept_colour_101, [1, 1, 1]
select pept_bond, (name ca,n and resi 101) or (name ca,c and resi 100)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_101, pept_bond
delete pept_bond

set_color pept_colour_103, [1, 1, 1]
select pept_bond, (name ca,n and resi 103) or (name ca,c and resi 102)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_103, pept_bond
delete pept_bond

set_color pept_colour_104, [1, 1, 1]
select pept_bond, (name ca,n and resi 104) or (name ca,c and resi 103)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_104, pept_bond
delete pept_bond

set_color pept_colour_105, [1, 1, 1]
select pept_bond, (name ca,n and resi 105) or (name ca,c and resi 104)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_105, pept_bond
delete pept_bond

set_color pept_colour_106, [0.207253395878, 0.724974030202, 0.848069223739]
select pept_bond, (name ca,n and resi 106) or (name ca,c and resi 105)
as sticks, pept_bond
set_bond stick_radius, 0.348578518903, pept_bond
set_bond stick_color, pept_colour_106, pept_bond
delete pept_bond

set_color pept_colour_107, [1, 1, 1]
select pept_bond, (name ca,n and resi 107) or (name ca,c and resi 106)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_107, pept_bond
delete pept_bond

set_color pept_colour_108, [1, 1, 1]
select pept_bond, (name ca,n and resi 108) or (name ca,c and resi 107)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_108, pept_bond
delete pept_bond

set_color pept_colour_109, [1, 1, 1]
select pept_bond, (name ca,n and resi 109) or (name ca,c and resi 108)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_109, pept_bond
delete pept_bond

set_color pept_colour_110, [1, 1, 1]
select pept_bond, (name ca,n and resi 110) or (name ca,c and resi 109)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_110, pept_bond
delete pept_bond

set_color pept_colour_111, [1, 1, 1]
select pept_bond, (name ca,n and resi 111) or (name ca,c and resi 110)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_111, pept_bond
delete pept_bond

set_color pept_colour_113, [1, 1, 1]
select pept_bond, (name ca,n and resi 113) or (name ca,c and resi 112)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_113, pept_bond
delete pept_bond

set_color pept_colour_114, [0.1557801459, 0.544920191633, 0.885802602209]
select pept_bond, (name ca,n and resi 114) or (name ca,c and resi 113)
as sticks, pept_bond
set_bond stick_radius, 0.758723937055, pept_bond
set_bond stick_color, pept_colour_114, pept_bond
delete pept_bond

set_color pept_colour_115, [1, 1, 1]
select pept_bond, (name ca,n and resi 115) or (name ca,c and resi 114)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_115, pept_bond
delete pept_bond

set_color pept_colour_116, [1, 1, 1]
select pept_bond, (name ca,n and resi 116) or (name ca,c and resi 115)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_116, pept_bond
delete pept_bond

set_color pept_colour_119, [0.224240827879, 0.784396202699, 0.835616285539]
select pept_bond, (name ca,n and resi 119) or (name ca,c and resi 118)
as sticks, pept_bond
set_bond stick_radius, 0.213220494992, pept_bond
set_bond stick_color, pept_colour_119, pept_bond
delete pept_bond

set_color pept_colour_121, [0.198083783869, 0.692898654331, 0.854791170391]
select pept_bond, (name ca,n and resi 121) or (name ca,c and resi 120)
as sticks, pept_bond
set_bond stick_radius, 0.421643156422, pept_bond
set_bond stick_color, pept_colour_121, pept_bond
delete pept_bond

set_color pept_colour_123, [1, 1, 1]
select pept_bond, (name ca,n and resi 123) or (name ca,c and resi 122)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_123, pept_bond
delete pept_bond

set_color pept_colour_124, [1, 1, 1]
select pept_bond, (name ca,n and resi 124) or (name ca,c and resi 123)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_124, pept_bond
delete pept_bond

set_color pept_colour_125, [0.208779373118, 0.730311910746, 0.846950579069]
select pept_bond, (name ca,n and resi 125) or (name ca,c and resi 124)
as sticks, pept_bond
set_bond stick_radius, 0.336419337708, pept_bond
set_bond stick_color, pept_colour_125, pept_bond
delete pept_bond

set_color pept_colour_126, [0.209996482682, 0.7345693697, 0.846058355325]
select pept_bond, (name ca,n and resi 126) or (name ca,c and resi 125)
as sticks, pept_bond
set_bond stick_radius, 0.326721253531, pept_bond
set_bond stick_color, pept_colour_126, pept_bond
delete pept_bond

set_color pept_colour_127, [1, 1, 1]
select pept_bond, (name ca,n and resi 127) or (name ca,c and resi 126)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_127, pept_bond
delete pept_bond

set_color pept_colour_129, [0.213142235309, 0.745573237456, 0.84375230559]
select pept_bond, (name ca,n and resi 129) or (name ca,c and resi 128)
as sticks, pept_bond
set_bond stick_radius, 0.301655495545, pept_bond
set_bond stick_color, pept_colour_129, pept_bond
delete pept_bond

set_color pept_colour_130, [1, 1, 1]
select pept_bond, (name ca,n and resi 130) or (name ca,c and resi 129)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_130, pept_bond
delete pept_bond

set_color pept_colour_131, [0.205164025793, 0.717665396996, 0.849600873523]
select pept_bond, (name ca,n and resi 131) or (name ca,c and resi 130)
as sticks, pept_bond
set_bond stick_radius, 0.365226886115, pept_bond
set_bond stick_color, pept_colour_131, pept_bond
delete pept_bond

set_color pept_colour_132, [1, 1, 1]
select pept_bond, (name ca,n and resi 132) or (name ca,c and resi 131)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_132, pept_bond
delete pept_bond

set_color pept_colour_133, [1, 1, 1]
select pept_bond, (name ca,n and resi 133) or (name ca,c and resi 132)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_133, pept_bond
delete pept_bond

set_color pept_colour_134, [1, 1, 1]
select pept_bond, (name ca,n and resi 134) or (name ca,c and resi 133)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_134, pept_bond
delete pept_bond

set_color pept_colour_135, [0.21033194006, 0.735742802283, 0.845812442346]
select pept_bond, (name ca,n and resi 135) or (name ca,c and resi 134)
as sticks, pept_bond
set_bond stick_radius, 0.324048286371, pept_bond
set_bond stick_color, pept_colour_135, pept_bond
delete pept_bond

set_color pept_colour_136, [0.196270377825, 0.686555345541, 0.856120519841]
select pept_bond, (name ca,n and resi 136) or (name ca,c and resi 135)
as sticks, pept_bond
set_bond stick_radius, 0.436092606969, pept_bond
set_bond stick_color, pept_colour_136, pept_bond
delete pept_bond

set_color pept_colour_137, [0.214289619393, 0.749586796124, 0.842911195345]
select pept_bond, (name ca,n and resi 137) or (name ca,c and resi 136)
as sticks, pept_bond
set_bond stick_radius, 0.292512992884, pept_bond
set_bond stick_color, pept_colour_137, pept_bond
delete pept_bond

set_color pept_colour_138, [0.200820838529, 0.70247289334, 0.852784723947]
select pept_bond, (name ca,n and resi 138) or (name ca,c and resi 137)
as sticks, pept_bond
set_bond stick_radius, 0.399833955944, pept_bond
set_bond stick_color, pept_colour_138, pept_bond
delete pept_bond

set_color pept_colour_139, [0.211949619978, 0.741401459523, 0.844626573403]
select pept_bond, (name ca,n and resi 139) or (name ca,c and resi 138)
as sticks, pept_bond
set_bond stick_radius, 0.311158406553, pept_bond
set_bond stick_color, pept_colour_139, pept_bond
delete pept_bond

set_color pept_colour_140, [1, 1, 1]
select pept_bond, (name ca,n and resi 140) or (name ca,c and resi 139)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_140, pept_bond
delete pept_bond

set_color pept_colour_141, [1, 1, 1]
select pept_bond, (name ca,n and resi 141) or (name ca,c and resi 140)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_141, pept_bond
delete pept_bond

set_color pept_colour_142, [0.203506969544, 0.711869001035, 0.850815607984]
select pept_bond, (name ca,n and resi 142) or (name ca,c and resi 141)
as sticks, pept_bond
set_bond stick_radius, 0.37843052156, pept_bond
set_bond stick_color, pept_colour_142, pept_bond
delete pept_bond

set_color pept_colour_143, [1, 1, 1]
select pept_bond, (name ca,n and resi 143) or (name ca,c and resi 142)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_143, pept_bond
delete pept_bond

set_color pept_colour_144, [1, 1, 1]
select pept_bond, (name ca,n and resi 144) or (name ca,c and resi 143)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_144, pept_bond
delete pept_bond

set_color pept_colour_145, [0.208253681107, 0.728473035903, 0.847335946918]
select pept_bond, (name ca,n and resi 145) or (name ca,c and resi 144)
as sticks, pept_bond
set_bond stick_radius, 0.340608118672, pept_bond
set_bond stick_color, pept_colour_145, pept_bond
delete pept_bond

set_color pept_colour_146, [0.188866265065, 0.660655700109, 0.861548235968]
select pept_bond, (name ca,n and resi 146) or (name ca,c and resi 145)
as sticks, pept_bond
set_bond stick_radius, 0.495089521391, pept_bond
set_bond stick_color, pept_colour_146, pept_bond
delete pept_bond

set_color pept_colour_147, [0.203266505278, 0.711027855115, 0.850991884577]
select pept_bond, (name ca,n and resi 147) or (name ca,c and resi 146)
as sticks, pept_bond
set_bond stick_radius, 0.380346571491, pept_bond
set_bond stick_color, pept_colour_147, pept_bond
delete pept_bond

set_color pept_colour_148, [0.201852785551, 0.706082652245, 0.852028236887]
select pept_bond, (name ca,n and resi 148) or (name ca,c and resi 147)
as sticks, pept_bond
set_bond stick_radius, 0.391611270513, pept_bond
set_bond stick_color, pept_colour_148, pept_bond
delete pept_bond

set_color pept_colour_149, [1, 1, 1]
select pept_bond, (name ca,n and resi 149) or (name ca,c and resi 148)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_149, pept_bond
delete pept_bond

set_color pept_colour_150, [0.207988059459, 0.727543889261, 0.847530665576]
select pept_bond, (name ca,n and resi 150) or (name ca,c and resi 149)
as sticks, pept_bond
set_bond stick_radius, 0.342724625828, pept_bond
set_bond stick_color, pept_colour_150, pept_bond
delete pept_bond

set_color pept_colour_152, [1, 1, 1]
select pept_bond, (name ca,n and resi 152) or (name ca,c and resi 151)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_152, pept_bond
delete pept_bond

set_color pept_colour_153, [1, 1, 1]
select pept_bond, (name ca,n and resi 153) or (name ca,c and resi 152)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_153, pept_bond
delete pept_bond

set_color pept_colour_154, [0.198458892469, 0.694210787202, 0.854516190381]
select pept_bond, (name ca,n and resi 154) or (name ca,c and resi 153)
as sticks, pept_bond
set_bond stick_radius, 0.418654243276, pept_bond
set_bond stick_color, pept_colour_154, pept_bond
delete pept_bond

set_color pept_colour_155, [1, 1, 1]
select pept_bond, (name ca,n and resi 155) or (name ca,c and resi 154)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_155, pept_bond
delete pept_bond

set_color pept_colour_156, [0.224041168499, 0.783697792599, 0.835762649387]
select pept_bond, (name ca,n and resi 156) or (name ca,c and resi 155)
as sticks, pept_bond
set_bond stick_radius, 0.214811406381, pept_bond
set_bond stick_color, pept_colour_156, pept_bond
delete pept_bond

set_color pept_colour_157, [1, 1, 1]
select pept_bond, (name ca,n and resi 157) or (name ca,c and resi 156)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_157, pept_bond
delete pept_bond

set_color pept_colour_158, [1, 1, 1]
select pept_bond, (name ca,n and resi 158) or (name ca,c and resi 157)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_158, pept_bond
delete pept_bond

set_color pept_colour_159, [0.199726982992, 0.698646577958, 0.853586594141]
select pept_bond, (name ca,n and resi 159) or (name ca,c and resi 158)
as sticks, pept_bond
set_bond stick_radius, 0.408549936315, pept_bond
set_bond stick_color, pept_colour_159, pept_bond
delete pept_bond

set_color pept_colour_160, [0.215266811437, 0.753005021681, 0.842194847393]
select pept_bond, (name ca,n and resi 160) or (name ca,c and resi 159)
as sticks, pept_bond
set_bond stick_radius, 0.284726602094, pept_bond
set_bond stick_color, pept_colour_160, pept_bond
delete pept_bond

set_color pept_colour_161, [0.20917594671, 0.731699128332, 0.846659863767]
select pept_bond, (name ca,n and resi 161) or (name ca,c and resi 160)
as sticks, pept_bond
set_bond stick_radius, 0.333259388766, pept_bond
set_bond stick_color, pept_colour_161, pept_bond
delete pept_bond

set_color pept_colour_162, [1, 1, 1]
select pept_bond, (name ca,n and resi 162) or (name ca,c and resi 161)
as sticks, pept_bond
set_bond stick_radius, 0.3, pept_bond
set_bond stick_color, pept_colour_162, pept_bond
delete pept_bond
