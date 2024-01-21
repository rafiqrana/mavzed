# MAV-ZED: A ZED Stereo Camera Controller
MAV-ZED is a MAVLINK based zed stereo camera controller which is packaged using the latest snapcraft linux packaging infrastructure. 

## Build pip (whell)

```bash
python3 -m build
```

## Build snap package

```bash
cd <project_dir>
snapcraft
```
### Install mavzed snap

```bash
sudo snap install <path_to_snap.snap> --dangerous
``` 
### Uninstall mavzed snap

```bash
sudo snap uninstall mavzed
```
