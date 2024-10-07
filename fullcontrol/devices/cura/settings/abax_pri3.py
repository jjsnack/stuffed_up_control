default_initial_settings = {
    "name": "Abax PRi3",
    "manufacturer": "Abax 3D Technologies",
    "start_gcode": "; -- START GCODE --\nG21                     ;set units to millimetres\nG90                     ;set to absolute positioning\nM106 S0                 ;set fan speed to zero (turned off)\nG28 X0 Y0               ;move to the X/Y origin (Home)\nG28 Z0                  ;move to the Z origin (Home)\nG1 Z5.0 F200          ;move Z to position 5.0 mm\nG92 E0                  ;zero the extruded length\n; -- end of START GCODE --",
    "end_gcode": "; -- END GCODE --\nM104 S0                 ;set extruder temperature to zero (turned off)\nM140 S0  ;set temp of bed to Zero  \nG91                     ;set to relative positioning\nG1 E-10 F300            ;retract the filament a bit to release some of the pressure\nG1 F2000 X0 Y215                 ;move X to min and Y to max \nG90                     ;set to absolute positioning\nM84                     ;turn off steppers\n; -- end of END GCODE --",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 40,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 225,
    "build_volume_y": 220,
    "build_volume_z": 200,
}