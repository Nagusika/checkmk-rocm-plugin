# ROCm SMI Monitoring Plugin for CheckMK

## Overview
This plugin provides comprehensive monitoring for AMD GPUs using the `rocm-smi` command, integrated with the CheckMK monitoring system.

## Features
- GPU Utilization Tracking
- Memory Utilization Monitoring
- Temperature Tracking
- Power Consumption Monitoring (Draw)
- SCLK Clock Frequency Monitoring
- Performance Level Tracking
- Memory Usage Monitoring
- Number of Active Processes

## Components
- `agent/rocm-smi`: Agent-side script to collect GPU metrics
- `server/rocm-smi`: CheckMK server-side plugin for parsing and monitoring GPU data

## Requirements
- AMD GPU supporting ROCm
- CheckMK Monitoring System
- Python 3.x
- `rocm-smi` command-line tool

## Installation

1. **Login to CheckMK Server**
   
2. **Download the Latest Release Plugin**
   ```bash
   wget https://git.pabr.de/paul/rocm-smi-plugin/archive/refs/tags/v1.0.1.tar.gz
   tar -xzvf v1.0.1.tar.gz
   cd rocm-smi-plugin-1.0.1
   ```

3. **Install the Plugin**
   ```bash
   mkp install rocm-smi-1.0.1.mkp
   ```

4. **List the Installed Plugin**
   ```bash
   mkp list rocm_smi
   ```

5. **Copy the Agent Plugin**
   ```bash
   cp agents/rocm-smi /omd/sites/test/local/lib/check_mk_agent/plugins/rocm-smi
   chmod +x /omd/sites/test/local/lib/check_mk_agent/plugins/rocm-smi
   ```

6. **Copy the Server Plugin**
   ```bash
   cp server/rocm-smi /omd/sites/test/local/share/check_mk/web/plugins/rocm-smi
   chmod +x /omd/sites/test/local/share/check_mk/web/plugins/rocm-smi
   ```

7. **Copy the CheckMK Plugin**
   ```bash
   cp checkman/rocm-smi /omd/sites/test/local/share/check_mk/web/plugins/rocm-smi
   chmod +x /omd/sites/test/local/share/check_mk/web/plugins/rocm-smi
   ```

8. **Copy the Metrics Plugin**
   ```bash
   cp cmk_addons_plugins/rocm-smi.py /omd/sites/test/local/lib/check_mk/base/plugins/agent_based/rocm_smi.py
   ```

9. **Run Host Full Scan**
   - Navigate to your CheckMK web interface.
   - Go to **Hosts** > **Full Scan** to discover the new GPU services.

## Metrics Collected
- **GPU Utilization (`gpu_utilization`)**
  - **Description:** Percentage of GPU usage.
  - **Unit:** `%`

- **Memory Utilization (`memory_utilization`)**
  - **Description:** Percentage of VRAM allocated.
  - **Unit:** `%`

- **Temperature (`temperature`)**
  - **Description:** GPU junction temperature.
  - **Unit:** `°C`

- **Power Draw (`power_draw`)**
  - **Description:** Current power consumption in Watts.
  - **Unit:** `W`

- **SCLK Clock Frequency (`sclk_clock_freq`)**
  - **Description:** Current SCLK (System Clock) frequency.
  - **Unit:** `MHz`

- **Performance Level (`performance_level`)**
  - **Description:** Current performance state of the GPU.
  - **Unit:** *None*

- **Memory Used (`memory_used`)**
  - **Description:** Amount of VRAM used.
  - **Unit:** `MB`

- **Number of GPU Processes (`num_processes`)**
  - **Description:** Number of active processes utilizing the GPU.
  - **Unit:** *None*

## License
MIT License - See [LICENSE](LICENSE) file for details.

