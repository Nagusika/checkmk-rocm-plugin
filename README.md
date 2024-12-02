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

### **Key Changes:**

- **Title and Overview:** Changed from NVIDIA to AMD and `nvidia-smi` to `rocm-smi`.
- **Features:** Updated to include metrics relevant to `rocm-smi` and removed obsolete ones.
- **Components:** Renamed scripts and paths to reflect `rocm-smi`.
- **Installation:** Updated installation steps to use `rocm-smi` instead of `nvidia-smi`. Adjusted file paths accordingly.
- **Metrics Collected:** Updated the list to include new metrics (`sclk_clock_freq`, `performance_level`) and removed obsolete ones (`fan_speed`, `ecc_errors_single_bit`, `ecc_errors_double_bit`, `power_limit`, `max_memory`).
- **License Section:** Updated to reference the MIT License and included a link to the LICENSE file.

---

## 4. Additional Recommendations

### **A. Updating File Paths and Names**

Ensure that all file paths and names in your project directory structure reflect the changes from NVIDIA to AMD. For example:

- **Agent Script:** `agent/rocm-smi`
- **Server Plugin:** `server/rocm-smi`
- **CheckMK Plugin:** `checkman/rocm-smi`
- **Metrics Plugin:** `cmk_addons_plugins/rocm-smi.py`

### **B. Updating `rocm-smi.py` Metrics**

Make sure that your `rocm-smi.py` scr# ROCm SMI Monitoring Plugin for CheckMK

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

### **Key Changes:**

- **Title and Overview:** Changed from NVIDIA to AMD and `nvidia-smi` to `rocm-smi`.
- **Features:** Updated to include metrics relevant to `rocm-smi` and removed obsolete ones.
- **Components:** Renamed scripts and paths to reflect `rocm-smi`.
- **Installation:** Updated installation steps to use `rocm-smi` instead of `nvidia-smi`. Adjusted file paths accordingly.
- **Metrics Collected:** Updated the list to include new metrics (`sclk_clock_freq`, `performance_level`) and removed obsolete ones (`fan_speed`, `ecc_errors_single_bit`, `ecc_errors_double_bit`, `power_limit`, `max_memory`).
- **License Section:** Updated to reference the MIT License and included a link to the LICENSE file.

---

## 4. Additional Recommendations

### **A. Updating File Paths and Names**

Ensure that all file paths and names in your project directory structure reflect the changes from NVIDIA to AMD. For example:

- **Agent Script:** `agent/rocm-smi`
- **Server Plugin:** `server/rocm-smi`
- **CheckMK Plugin:** `checkman/rocm-smi`
- **Metrics Plugin:** `cmk_addons_plugins/rocm-smi.py`

### **B. Updating `rocm-smi.py` Metrics**

Make sure that your `rocm-smi.py` script accurately references the new metrics defined in `metric_info` and aligns with the `graph_info` configurations. Here's a quick checklist:

- **Remove References** to obsolete NVIDIA-specific metrics.
- **Add References** to new AMD-specific metrics like `sclk_clock_freq` and `performance_level`.
- **Ensure Consistency** between `metric_info`, `graph_info`, and the server-side check plugins.

### **C. Testing**

After making all the updates:

1. **Deploy the Updated Plugins and Scripts**
   - Ensure that all scripts have the correct permissions (`chmod +x`) and are placed in their respective directories.

2. **Run a Full Host Scan in CheckMK**
   - This will discover the new AMD GPU services based on the updated plugins.

3. **Verify Metrics Collection**
   - Check the CheckMK web interface to ensure that all metrics are being collected and displayed correctly.
   - Test threshold alerts by simulating high utilization or temperature if possible.

4. **Review Logs for Errors**
   - Check CheckMK and agent logs to ensure there are no parsing or execution errors.

### **D. Documentation and Support**

- **Document Changes:** Keep a changelog or update your documentation to reflect the transition from NVIDIA to AMD monitoring.
- **User Guidance:** Update any user guides or support materials to assist users in migrating to the new AMD monitoring setup.

---

## 5. Example Directory Structure

Here's an example of how your project directory might look after the updates:
```
rocm-smi-plugin/
├── LICENSE
├── README.md
├── rocm-smi.manifest
├── agent/
│   └── rocm-smi
├── server/
│   └── rocm-smi
├── checkman/
│   └── rocm-smi
└── cmk_addons_plugins/
    └── rocm-smi.py
```

Ensure that each script is correctly referenced in the `rocm-smi.manifest` and that all paths are accurate during installation.
ipt accurately references the new metrics defined in `metric_info` and aligns with the `graph_info` configurations. Here's a quick checklist:

- **Remove References** to obsolete NVIDIA-specific metrics.
- **Add References** to new AMD-specific metrics like `sclk_clock_freq` and `performance_level`.
- **Ensure Consistency** between `metric_info`, `graph_info`, and the server-side check plugins.

### **C. Testing**

After making all the updates:

1. **Deploy the Updated Plugins and Scripts**
   - Ensure that all scripts have the correct permissions (`chmod +x`) and are placed in their respective directories.

2. **Run a Full Host Scan in CheckMK**
   - This will discover the new AMD GPU services based on the updated plugins.

3. **Verify Metrics Collection**
   - Check the CheckMK web interface to ensure that all metrics are being collected and displayed correctly.
   - Test threshold alerts by simulating high utilization or temperature if possible.

4. **Review Logs for Errors**
   - Check CheckMK and agent logs to ensure there are no parsing or execution errors.

### **D. Documentation and Support**

- **Document Changes:** Keep a changelog or update your documentation to reflect the transition from NVIDIA to AMD monitoring.
- **User Guidance:** Update any user guides or support materials to assist users in migrating to the new AMD monitoring setup.

---

## 5. Example Directory Structure

Here's an example of how your project directory might look after the updates:
```
rocm-smi-plugin/
├── LICENSE
├── README.md
├── rocm-smi.manifest
├── agent/
│   └── rocm-smi
├── server/
│   └── rocm-smi
├── checkman/
│   └── rocm-smi
└── cmk_addons_plugins/
    └── rocm-smi.py
```

Ensure that each script is correctly referenced in the `rocm-smi.manifest` and that all paths are accurate during installation.
