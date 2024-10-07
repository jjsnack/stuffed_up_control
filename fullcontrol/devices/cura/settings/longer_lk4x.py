default_initial_settings = {
    "name": "Longer LK4 X",
    "manufacturer": "Longer",
    "start_gcode": "; -- LONGER BL-TOUCH Start G-code --\nG21 ; metric values\nG90 ; absolute positioning\nM82 ; set extruder to absolute mode\nM107 ; start with the fan off\n\n; confirm BL-touch safety\nM280 P0 S160 ; BL-Touch Alarm release\nG4 P100 ; Delay for BL-Touch\n\n; homing\nG28 X0 Y0 ; move X/Y to min endstops\nG28 Z0 ; move Z to min endstops\n\n; reconfirm BL-touch safety\nM280 P0 S160 ; BL-Touch Alarm realease\nG4 P100 ; Delay for BL-Touch\n\n; bed leveling\nG29; Auto leveling\nM420 Z5 ; set LEVELING_FADE_HEIGHT\nM500 ; save data of G29 and M420\nM420 S1 ; enable bed leveling\n\n; prepare hot-end\nG92 E0 ; Reset Extruder\nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\nG1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position\nG1 X0.1 Y150.0 Z0.3 F1500.0 E15 ; Draw the first line\nG1 X0.4 Y150.0 Z0.3 F5000.0 ; Move to side a little\nG1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line\nG92 E0 ; Reset Extruder\nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\nG1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish\n; -- end of LONGER BL-TOUCH Start G-code --",
    "end_gcode": "; LONGER End G-code\nG91 ;Relative positioning\nG1 E-2 F2700 ;Retract a bit\nG1 E-2 Z0.2 F2400 ;Retract and raise Z\nG1 X5 Y5 F3000 ;Wipe out\nG1 Z10 ;Raise Z more\nG90 ;Absolute positioning\nG1 X0 Y{data['build_volume_y']} ;Present print\nM106 S0 ;Turn-off fan\nM104 S0 ;Turn-off hotend\nM140 S0 ;Turn-off bed\nM84 X Y E ;Disable all steppers but Z\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 50.0,
    "travel_speed": 65,
    "dia_feed": 1.75,
    "build_volume_x": 220,
    "build_volume_y": 220,
    "build_volume_z": 250,
}