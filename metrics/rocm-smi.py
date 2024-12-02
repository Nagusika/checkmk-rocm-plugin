metric_info = {}

# Existing Metrics
metric_info["gpu_utilization"] = {
    "title" : _("GPU Utilization"),
    "unit"  : "%",
    "color" : "31/a",
}

metric_info["memory_utilization"] = {
    "title" : _("Memory Utilization"),
    "unit"  : "%",
    "color" : "21/b",
}

metric_info["temperature"] = {
    "title" : _("Temperature"),
    "unit"  : "°C",
    "color" : "41/b",
}

metric_info["power_draw"] = {
    "title" : _("Power Draw"),
    "unit"  : "W",
    "color" : "42/a",
}

metric_info["memory_used"] = {
    "title" : _("Memory Used"),
    "unit"  : "MB",
    "color" : "21/a",
}

metric_info["num_processes"] = {
    "title" : _("Number of GPU Processes"),
    "unit"  : "",
    "color" : "36/a",
}

# New Metrics
metric_info["sclk_clock_freq"] = {
    "title" : _("SCLK Clock Frequency"),
    "unit"  : "MHz",
    "color" : "35/a",
}

metric_info["performance_level"] = {
    "title" : _("Performance Level"),
    "unit"  : "",
    "color" : "53/a",
}

metric_info["pci_bus"] = {
    "title" : _("PCI Bus ID"),
    "unit"  : "",
    "color" : "52/a",
}

graph_info = []

# Existing Graphs
graph_info.append({
    "title"   : _("GPU Utilization"),
    "metrics" : [
        ("gpu_utilization", "area"),
        ("memory_utilization", "line"),
    ],
})

graph_info.append({
    "title"   : _("Memory Usage"),
    "metrics" : [
        ("memory_used", "line"),
        ("memory_total", "line"),
    ],
})

graph_info.append({
    "title"   : _("GPU Processes"),
    "metrics" : [
        ("num_processes", "line"),
    ],
})

# New Graphs
graph_info.append({
    "title"   : _("SCLK Clock Frequency"),
    "metrics" : [
        ("sclk_clock_freq", "line"),
    ],
})

graph_info.append({
    "title"   : _("Performance Level"),
    "metrics" : [
        ("performance_level", "line"),
    ],
})