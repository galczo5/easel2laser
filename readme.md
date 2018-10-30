# easel2laser

Simple python script that converts Easel gcode file for use with chinese-made grbl devices.

Script removes all `M3` and `M4` commands in original file, disables laser before Z-axis up move and enables it after Z-axis down move. Laser is enabled and disabled with `M3` command .`S` value of enabled and disabled value can be configured.

Please remember to set *Safety Height* in Easel to provide Z-axis movment.

## Usage
```
git clone https://github.com/galczo5/easel2laser.git
cd easel2laser
./easel2laser.py <input-file-path> <output-file-path> <S-value-laser-on>  <S-value-laser-off>
```

## Contributing
Please leave issue or open pull request if you have ideas for development of this script.

## License
MIT
