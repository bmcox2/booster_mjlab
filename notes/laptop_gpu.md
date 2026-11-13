# Laptop GPU: known problems and fixes

Dell XPS 15, RTX 4070 Laptop 8 GB, Ubuntu 24.04 (dual boot). Moved here from `CLAUDE.md` on 2026-11-13.

## Basics
- GPU power capped ~35 W. 4096 envs fit in 8 GB (~3k iterations ≈ 2.5 h for the velocity task).
- Check `nvidia-smi` before runs; stop if the GPU sustains > ~87 °C. The laptop has overheated before.
- Prefer the club GPU PC for long runs (`CLAUDE.md`, Environment).

## `nvidia-smi` fails after a kernel update (2026-10-19)
The NVIDIA module package wasn't updated with the kernel, so the GPU runs with no driver, stuck at
full power (loud fans at idle). Fix: `sudo apt install linux-modules-nvidia-595-open-generic-hwe-24.04`,
then reboot. Use `sudo apt full-upgrade` (not `upgrade`) for kernel updates.

## dGPU dropouts are hardware (journal analysis 2026-10-19)
- Every failure is the PCIe link failing to come back when the GPU powers up
  (`pcieport 0000:00:01.0: retraining failed` → Xid 79 / `GSP boot failed at resume`), after suspend or
  runtime power-off. It never failed under load.
- Sometimes it also fails at cold boot, and then the BIOS hides the GPU for days (09-09→10-02,
  10-16→10-18, and again from before 2026-11-08: the speech loop was benchmarked CPU-only).
- **Don't** disable runtime power-off (`NVreg_DynamicPowerManagement=0x00`) to avoid this: the awake GPU
  idles at ~25 W at P8 (fans ~5,000 RPM). Tried and reverted 2026-10-19.
- Mitigations kept: lid close → power off (`/etc/systemd/logind.conf.d/lid-poweroff.conf`), no
  auto-suspend on battery.
- To override `/lib/modprobe.d/nvidia-runtimepm.conf` (`0x02`), a file in `/etc/modprobe.d/` must have
  the **same name**, then `sudo update-initramfs -u`. Live value: `grep DynamicPower /proc/driver/nvidia/params`.

## Long CPU builds
`tools/laptop_build_governor.sh` cycles load to keep temperatures down during long dataset builds
(use `OMP_NUM_THREADS=1` workers).
