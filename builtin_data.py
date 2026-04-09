"""
内置 BSP 数据 — 直接从 HTML 提取，共 224 条
in_str=True 表示该条已在 STR 分支合入
"""

BSP_DATA = [
  {
    "jira": "IVI8397-2660",
    "subject": "Fix issues in GPU",
    "type": "bugfix",
    "function": "GPU",
    "repo": "apps_proc/prebuilt_HY11",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 0
  },
  {
    "jira": "IVI8397-2546",
    "subject": "ufs bug fix",
    "type": "bugfix",
    "function": "EVS",
    "repo": "meta-qti-auto-kernel",
    "owner": "xuejihuang",
    "in_str": True,
    "id": 1
  },
  {
    "jira": "IVI8397-2540",
    "subject": "Delete conflicting gpio configurations",
    "type": "Bugfix",
    "function": "STR",
    "repo": "vendor/proprietary",
    "owner": "mingkunye",
    "in_str": True,
    "id": 2
  },
  {
    "jira": "IVI8397-2546",
    "subject": "fix camera clock",
    "type": "bugfix",
    "function": "EVS",
    "repo": "amss_standard_oem",
    "owner": "xuejihuang",
    "in_str": True,
    "id": 3
  },
  {
    "jira": "IVI8397-2546",
    "subject": "fix camera clock",
    "type": "bugfix",
    "function": "EVS",
    "repo": "vendor/proprietary",
    "owner": "xuejihuang",
    "in_str": True,
    "id": 4
  },
  {
    "jira": "IVI8397-2643",
    "subject": "change max96724 the way of powerof",
    "type": "Bugfix",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "yupan1",
    "in_str": False,
    "id": 7
  },
  {
    "jira": "IVI8397-2900",
    "subject": "Fixing configuration file issues for H47A and BSP.",
    "type": "bugfix",
    "function": "diag",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 8
  },
  {
    "jira": "IVI8397-822",
    "subject": "modify a2b log and capture ref channel",
    "type": "features",
    "function": "audio",
    "repo": "voyah-bsp",
    "owner": "h-huzhonghua",
    "in_str": False,
    "id": 9
  },
  {
    "jira": "IVI8397-2899",
    "subject": "update display diag",
    "type": "bugfix",
    "function": "diag",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 10
  },
  {
    "jira": "IVI8397-57",
    "subject": "合入V0.0.09蓝牙和副蓝牙协议栈 1.解决蓝牙设备名显示异常的问题",
    "type": "feature",
    "function": "BT",
    "repo": "vendor/quectel",
    "owner": "guijunzhou",
    "in_str": False,
    "id": 11
  },
  {
    "jira": "IVI8397-2762",
    "subject": "默认开启AVM低帧率检测",
    "type": "feature",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "h-ligang1",
    "in_str": False,
    "id": 12
  },
  {
    "jira": "IVI8397-2886",
    "subject": "Fixed an issue where factory reset failed due to umount failure.",
    "type": "bugfix",
    "function": "recovery",
    "repo": "meta-voyah-bsp",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 13
  },
  {
    "jira": "IVI8397-2052",
    "subject": "optimize spi cs, spi-patch from Qualcomm.",
    "type": "feature",
    "function": "spi-driver",
    "repo": "meta-voyah-bsp",
    "owner": "wangyang1",
    "in_str": False,
    "id": 14
  },
  {
    "jira": "IVI8397-56",
    "subject": "开机时间优化|取消recovery的preload",
    "type": "Feature",
    "function": "performance",
    "repo": "early-ramdisk-init",
    "owner": "yitianye",
    "in_str": False,
    "id": 16
  },
  {
    "jira": "IVI8397-2194",
    "subject": "串口加时间戳打印",
    "type": "Feature",
    "function": "log",
    "repo": "kernel/qcom",
    "owner": "yitianye",
    "in_str": False,
    "id": 17
  },
  {
    "jira": "IVI8397-2194",
    "subject": "gvmdump trigger fulldump for qcom",
    "type": "Feature",
    "function": "log",
    "repo": "qcom-opensource/devicetree",
    "owner": "chengzhou",
    "in_str": False,
    "id": 18
  },
  {
    "jira": "IVI8397-86",
    "subject": "Fix drm LUTDMA VQ busy status",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "h-huangyiran",
    "in_str": False,
    "id": 19
  },
  {
    "jira": "IVI8397-86",
    "subject": "set selinux=permissive",
    "type": "bugfix",
    "function": "STR",
    "repo": "qcom/gen5_gvm",
    "owner": "chengzhou",
    "in_str": False,
    "id": 20
  },
  {
    "jira": "IVI8397-168",
    "subject": "close tlmm-gpio on pvm drivers.",
    "type": "feature",
    "function": "test-str",
    "repo": "base-devicetree",
    "owner": "wangyang1",
    "in_str": False,
    "id": 22
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6711112 disp-msm-sde-guard-the-lutdma-interrupts",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 23
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6679173 disp-msm-sde-defer-the-LUTDMA-trigger",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 24
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6653085 sdm-fix-the-issue-of-error-max-mixer-stages",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 25
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6641777 config-enable-option-for-scaler-on-non-primary",
    "type": "bugfix",
    "function": "STR",
    "repo": "qcom/display",
    "owner": "chengzhou",
    "in_str": False,
    "id": 26
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6641482 sdm-add-option-to-allow-scaler-on-non-primary",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 27
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6614275 disp-msm-sde-split-large-LUTDMA-workload",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 28
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6610165 sdm-Only-check-EnableRc-for-displays",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 29
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6602967 sdm-add-rounded-corner-support (pateo)",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 30
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6603629 sdmclient-remove-CallDisplayFunction",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 31
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6603418 composer-Add-support-for-Display-Decoration",
    "type": "bugfix",
    "function": "STR",
    "repo": "qcom/display",
    "owner": "chengzhou",
    "in_str": False,
    "id": 32
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6603241 disp-msm-hyp-enable-rounded-corner-feature",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 33
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6601789 msm-Modify-log-level",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 35
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6556465 disp-msm-sde-fixed-issue-of-dim-layer-programming",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 36
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6552740 ARM-dts-msm-UBWC-setting-change",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-devicetree",
    "owner": "chengzhou",
    "in_str": False,
    "id": 37
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6551619 disp-msm-sde-UBWC-setting-change",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 38
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6548293 sdm-add-two-format-conversion-functions",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 39
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6538289 sdm-add-DPU-id-for-HWInfoDRM-log",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 40
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6535599 snapalloc-fix-the-marking-error",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 41
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6534987 disp-msm-sde-check-DPUID-on-register-HPD",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 42
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6522570 sdm-remove-check-of-first_cycle",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 43
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6490053 Revert-disp-msm-hyp-send-virtio-cmd-twice",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 44
  },
  {
    "jira": "IVI8397-2194",
    "subject": "qcrosvm_sa8797.service del owfd",
    "type": "feature",
    "function": "log",
    "repo": "crosvm-gunyah",
    "owner": "chengzhou",
    "in_str": False,
    "id": 45
  },
  {
    "jira": "IVI8397-2194",
    "subject": "gvm dump触发整机fulldump|only for debug",
    "type": "Feature",
    "function": "log",
    "repo": "gunyah-drivers",
    "owner": "yitianye",
    "in_str": False,
    "id": 47
  },
  {
    "jira": "H47A-4157",
    "subject": "使能MAX96792 PIPE操作，cable link延迟上报，增加热插拔出流稳定性",
    "type": "Bugfix",
    "function": "AVM",
    "repo": "vendor/proprietary",
    "owner": "h-ligang1",
    "in_str": False,
    "id": 48
  },
  {
    "jira": "H47A-3865",
    "subject": "remove mapping PHY to control single stream instead of pipe",
    "type": "Bugfix",
    "function": "AVM streaming",
    "repo": "vendor/proprietary",
    "owner": "jiashuhou",
    "in_str": False,
    "id": 49
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6562136 disp-msm-sde-set-encoder-old_state-to-NULL",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 50
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6470487 disp-msm-sde-reduce-VQ-done-waiting-interval",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 51
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR:6479053 display-core-fix-Android-16-compiler-issues",
    "type": "bugfix",
    "function": "STR",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 52
  },
  {
    "jira": "IVI8397-2866",
    "subject": "Android QCX EVSHAL支持热插拔",
    "type": "feature",
    "function": "EVS",
    "repo": "proprietary/qcx",
    "owner": "h-ligang1",
    "in_str": False,
    "id": 53
  },
  {
    "jira": "IVI8397-2194",
    "subject": "保存gvm dump到/rawdump目录",
    "type": "Feature",
    "function": "log",
    "repo": "vendor/proprietary",
    "owner": "yitianye",
    "in_str": False,
    "id": 54
  },
  {
    "jira": "IVI8397-111",
    "subject": "WiFi/BT device tree update",
    "type": "feature",
    "function": "BT/WIFI",
    "repo": "qcom-opensource/devicetree",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 56
  },
  {
    "jira": "IVI8397-111",
    "subject": "fixing the DMA unmap ordering",
    "type": "feature",
    "function": "uart",
    "repo": "kernel/qcom",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 57
  },
  {
    "jira": "IVI8397-2531",
    "subject": "Add temp monitor build",
    "type": "feature",
    "function": "log",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 58
  },
  {
    "jira": "IVI8397-1883",
    "subject": "enable ccidbgr for qcx server",
    "type": "feature",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "h-ligang1",
    "in_str": False,
    "id": 59
  },
  {
    "jira": "IVI8397-2836",
    "subject": "修正qcx evshal OMS RGB分辨率配置",
    "type": "bugfix",
    "function": "EVS",
    "repo": "proprietary/qcx",
    "owner": "h-ligang1",
    "in_str": False,
    "id": 60
  },
  {
    "jira": "IVI8397-2047",
    "subject": "modify groupconfig.xml for recovery function",
    "type": "feature",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "jiashuhou",
    "in_str": False,
    "id": 61
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Add support for multiple EVS instances",
    "type": "bugfix",
    "function": "EVS",
    "repo": "proprietary/qcx",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 62
  },
  {
    "jira": "IVI8397-2194",
    "subject": "fix la_gvm log to /data/logs",
    "type": "feature",
    "function": "log",
    "repo": "crosvm-gunyah",
    "owner": "chengzhou",
    "in_str": False,
    "id": 63
  },
  {
    "jira": "IVI8397-2531",
    "subject": "Add temp monitor",
    "type": "feature",
    "function": "log",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 64
  },
  {
    "jira": "IVI8397-2633",
    "subject": "增加CCI报错地址打印，方便定位哪个外设报错",
    "type": "Feature",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "h-ligang1",
    "in_str": False,
    "id": 65
  },
  {
    "jira": "IVI8397-2531",
    "subject": "Fix build error: scripts/basic/fixdep: Permission denied",
    "type": "bug",
    "function": "build",
    "repo": "kernel/qcom",
    "owner": "chengzhou",
    "in_str": False,
    "id": 66
  },
  {
    "jira": "IVI8397-2531",
    "subject": "Modify console loglevel",
    "type": "feature",
    "function": "log",
    "repo": "qcom/common",
    "owner": "chengzhou",
    "in_str": False,
    "id": 67
  },
  {
    "jira": "IVI8397-2194",
    "subject": "mv la_gvm log to /data/",
    "type": "feature",
    "function": "log",
    "repo": "crosvm-gunyah",
    "owner": "chengzhou",
    "in_str": False,
    "id": 68
  },
  {
    "jira": "IVI8397-2029",
    "subject": "la_gvm.txt循环保存",
    "type": "feature",
    "function": "log",
    "repo": "crosvm-gunyah",
    "owner": "chengzhou",
    "in_str": False,
    "id": 69
  },
  {
    "jira": "IVI8397-2747",
    "subject": "Fix issues in GPU|kiumd CR4394040",
    "type": "bugfix",
    "function": "GPU",
    "repo": "safelinux-cfg-modules",
    "owner": "yitianye",
    "in_str": False,
    "id": 70
  },
  {
    "jira": "IVI8397-2762",
    "subject": "增加AVM低帧率检测(默认关闭，可动态开关)",
    "type": "feature",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "h-ligang1",
    "in_str": False,
    "id": 71
  },
  {
    "jira": "IVI8397-369",
    "subject": "Secure Boot one-click signing script update",
    "type": "feature",
    "function": "Secure boot",
    "repo": "platform/build_repo",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 72
  },
  {
    "jira": "IVI8397-2052",
    "subject": "add dma flag in pvm,optimize data consistency",
    "type": "feature",
    "function": "dma-drivers",
    "repo": "base-devicetree",
    "owner": "wangyang1",
    "in_str": False,
    "id": 73
  },
  {
    "jira": "IVI8397-2052",
    "subject": "add spi-patch from Qualcomm,update spi resume.",
    "type": "feature",
    "function": "spi-driver",
    "repo": "meta-voyah-bsp",
    "owner": "wangyang1",
    "in_str": False,
    "id": 74
  },
  {
    "jira": "IVI8397-2052",
    "subject": "add dma flag in gvm,optimize data consistency.",
    "type": "feature",
    "function": "qup-driver",
    "repo": "qcom-opensource/devicetree",
    "owner": "wangyang1",
    "in_str": False,
    "id": 75
  },
  {
    "jira": "IVI8397-2693",
    "subject": "Completed the upgrade interfaces for OMS & DMS and optimized the exception handling of camera OTA.",
    "type": "Feature",
    "function": "Camera",
    "repo": "vendor/proprietary",
    "owner": "delisun",
    "in_str": False,
    "id": 76
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR: gearvm camera close",
    "type": "bugfix",
    "function": "STR",
    "repo": "amss_standard_oem",
    "owner": "chengzhou",
    "in_str": False,
    "id": 77
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR: gearvm camera close",
    "type": "bugfix",
    "function": "STR",
    "repo": "test_device",
    "owner": "chengzhou",
    "in_str": False,
    "id": 78
  },
  {
    "jira": "IVI8397-2366",
    "subject": "STR patch",
    "type": "feature",
    "function": "STR",
    "repo": "test_device",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 91
  },
  {
    "jira": "IVI8397-2366",
    "subject": "STR patch",
    "type": "feature",
    "function": "STR",
    "repo": "amss_standard_oem",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 94
  },
  {
    "jira": "IVI8397-2366",
    "subject": "STR patch",
    "type": "feature",
    "function": "STR",
    "repo": "vendor/proprietary",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 96
  },
  {
    "jira": "IVI8397-68",
    "subject": "Try fix HWInfoDRM::Init: Failed case08399776",
    "type": "feature",
    "function": "display",
    "repo": "opensource/display-drivers",
    "owner": "chengzhou",
    "in_str": False,
    "id": 97
  },
  {
    "jira": "IVI8397-2366",
    "subject": "Fix STR build error",
    "type": "feature",
    "function": "STR",
    "repo": "meta-qti-automotive-prop",
    "owner": "chengzhou",
    "in_str": False,
    "id": 99
  },
  {
    "jira": "IVI8397-29",
    "subject": "install qc-pm.h for powermanager",
    "type": "Feature",
    "function": "STR",
    "repo": "vendor/proprietary",
    "owner": "h-ligang1",
    "in_str": False,
    "id": 100
  },
  {
    "jira": "IVI8397-117",
    "subject": "modify BUS10_DOLBY output",
    "type": "Feature",
    "function": "Audio",
    "repo": "vendor/proprietary",
    "owner": "wenjuanli",
    "in_str": False,
    "id": 101
  },
  {
    "jira": "IVI8397-2726",
    "subject": "qcom patch for stability|linux wdog",
    "type": "bugfix",
    "function": "boot",
    "repo": "gunyah-drivers",
    "owner": "yitianye",
    "in_str": False,
    "id": 102
  },
  {
    "jira": "IVI8397-1883",
    "subject": "max96724 driver porting",
    "type": "bugfix",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "yupan1",
    "in_str": False,
    "id": 103
  },
  {
    "jira": "IVI8397-2642",
    "subject": "change the libgpio api from V1 toV2",
    "type": "Bugfix",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "yupan1",
    "in_str": False,
    "id": 106
  },
  {
    "jira": "IVI8397-1883",
    "subject": "临时解决stop oms时概率link lost导致不出流问题",
    "type": "bugfix",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "h-ligang1",
    "in_str": False,
    "id": 107
  },
  {
    "jira": "IVI8397-2660",
    "subject": "Fix issues in GPU",
    "type": "bugfix",
    "function": "GPU",
    "repo": "opensource/graphics-hgsl",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 108
  },
  {
    "jira": "IVI8397-2660",
    "subject": "Fix issues in GPU",
    "type": "bugfix",
    "function": "GPU",
    "repo": "proprietary/hgsl-devicetree",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 110
  },
  {
    "jira": "IVI8397-187",
    "subject": "IMU Selinux config, modify file_contexts and add hal_snesors_default.te.",
    "type": "Feature",
    "function": "imu-driver",
    "repo": "qcom/sepolicy_vndr",
    "owner": "wangyang1",
    "in_str": False,
    "id": 111
  },
  {
    "jira": "IVI8397-187",
    "subject": "IMU Selinux config, modify the ueventd configuration for IIO drivers.",
    "type": "Feature",
    "function": "imu-driver",
    "repo": "qcom/common",
    "owner": "wangyang1",
    "in_str": False,
    "id": 112
  },
  {
    "jira": "IVI8397-2674",
    "subject": "Adapting camera HAL to support multiple clients.",
    "type": "bugfix",
    "function": "camera",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 113
  },
  {
    "jira": "IVI8397-2047",
    "subject": "modify usecase xml to adapt multiclient function",
    "type": "feature",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "jiashuhou",
    "in_str": False,
    "id": 114
  },
  {
    "jira": "IVI8397-2531",
    "subject": "minicon hvc: add hvc1 console",
    "type": "feature",
    "function": "console",
    "repo": "qcom-opensource/devicetree",
    "owner": "chengzhou",
    "in_str": False,
    "id": 115
  },
  {
    "jira": "IVI8397-2531",
    "subject": "minicon hvc: update androidboot.consol to be hvc1,voyah",
    "type": "feature",
    "function": "console",
    "repo": "qcom/gen5_gvm",
    "owner": "chengzhou",
    "in_str": False,
    "id": 116
  },
  {
    "jira": "IVI8397-2531",
    "subject": "minicon hvc: allow hvc1 labeled as a console device",
    "type": "feature",
    "function": "console",
    "repo": "qcom/sepolicy_vndr",
    "owner": "chengzhou",
    "in_str": False,
    "id": 117
  },
  {
    "jira": "IVI8397-2531",
    "subject": "minicon hvc: enable hvc gunyah",
    "type": "feature",
    "function": "console",
    "repo": "kernel/qcom",
    "owner": "chengzhou",
    "in_str": False,
    "id": 118
  },
  {
    "jira": "IVI8397-123",
    "subject": "NFS功能 |NFS功能selinux执行权限tetest1",
    "type": "feature",
    "function": "",
    "repo": "qcom/sepolicy_vndr",
    "owner": "yitianye",
    "in_str": False,
    "id": 120
  },
  {
    "jira": "IVI8397-2338",
    "subject": "Try this patch in PVM for fix display ivi-shell str",
    "type": "bugfix",
    "function": "display",
    "repo": "opensource/display-core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 121
  },
  {
    "jira": "IVI8397-31",
    "subject": "Fixes the issue of incorrect ddr_lcp.elf path.",
    "type": "Feature",
    "function": "",
    "repo": "test_device",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 125
  },
  {
    "jira": "IVI8397-2531",
    "subject": "Fix dprx build error",
    "type": "feature",
    "function": "dprx",
    "repo": "meta-qti-automotive-prop",
    "owner": "chengzhou",
    "in_str": False,
    "id": 124
  },
  {
    "jira": "IVI8397-2531",
    "subject": "Auto enable dprx",
    "type": "feature",
    "function": "dprx",
    "repo": "meta-qti-automotive-prop",
    "owner": "chengzhou",
    "in_str": False,
    "id": 126
  },
  {
    "jira": "IVI8397-2531",
    "subject": "Auto enable dprx",
    "type": "feature",
    "function": "dprx",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 127
  },
  {
    "jira": "IVI8397-68",
    "subject": "Fix edk2 build error",
    "type": "feature",
    "function": "build",
    "repo": "meta-qti-automotive",
    "owner": "chengzhou",
    "in_str": False,
    "id": 128
  },
  {
    "jira": "IVI8397-2385",
    "subject": "Add eUSB2 PHY type support and fix USB compliance issues",
    "type": "feature",
    "function": "USB",
    "repo": "kernel/qcom",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 129
  },
  {
    "jira": "IVI8397-117",
    "subject": "add libfmpal libexterior_talk libswitch_tx",
    "type": "Feature",
    "function": "Audio",
    "repo": "qcom/gen5_gvm",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 130
  },
  {
    "jira": "IVI8397-117",
    "subject": "add radio driver code",
    "type": "Feature",
    "function": "Audio",
    "repo": "hardware/interfaces",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 131
  },
  {
    "jira": "IVI8397-117",
    "subject": "add awe xml",
    "type": "Feature",
    "function": "Audio",
    "repo": "proprietary/mm-audio-auto",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 132
  },
  {
    "jira": "IVI8397-117",
    "subject": "support multi-channels",
    "type": "Feature",
    "function": "Audio",
    "repo": "proprietary/mm-audio-headers",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 133
  },
  {
    "jira": "IVI8397-117",
    "subject": "add audio hal",
    "type": "Feature",
    "function": "Audio",
    "repo": "qcom/audio-ar",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 134
  },
  {
    "jira": "IVI8397-117",
    "subject": "add audio pal",
    "type": "Feature",
    "function": "Audio",
    "repo": "opensource/arpal-lx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 135
  },
  {
    "jira": "IVI8397-2366",
    "subject": "Add ADB security authentication (1/2)",
    "type": "feature",
    "function": "ADB",
    "repo": "modules/adb",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 139
  },
  {
    "jira": "IVI8397-2366",
    "subject": "Add ADB security authentication (2/2)",
    "type": "feature",
    "function": "ADB",
    "repo": "system/sepolicy",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 140
  },
  {
    "jira": "IVI8397-108",
    "subject": "Increase GVM memory size(2/2)",
    "type": "feature",
    "function": "GVM",
    "repo": "kernel/common",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 141
  },
  {
    "jira": "IVI8397-108",
    "subject": "Increase GVM memory size(1/2)",
    "type": "feature",
    "function": "GVM",
    "repo": "base-devicetree",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 142
  },
  {
    "jira": "H47A-367",
    "subject": "Enable MCC",
    "type": "feature",
    "function": "WLAN",
    "repo": "qcom/wlan",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 143
  },
  {
    "jira": "IVI8397-68",
    "subject": "audio adapt cs1 baseline",
    "type": "feature",
    "function": "audio",
    "repo": "voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 145
  },
  {
    "jira": "IVI8397-68",
    "subject": "display adapt cs1 baseline",
    "type": "feature",
    "function": "display",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 146
  },
  {
    "jira": "IVI8397-31",
    "subject": "reason is reboot send to pvm. Keep reason is shutdown",
    "type": "feature",
    "function": "system",
    "repo": "system/core",
    "owner": "chengzhou",
    "in_str": False,
    "id": 147
  },
  {
    "jira": "IVI8397-108",
    "subject": "Fix BT power on issue",
    "type": "feature",
    "function": "BT",
    "repo": "test_device",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 148
  },
  {
    "jira": "IVI8397-108",
    "subject": "Fix BT power on issue",
    "type": "feature",
    "function": "BT",
    "repo": "amss_standard_oem",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 149
  },
  {
    "jira": "IVI8394-44",
    "subject": "Resolves the issue of abnormal EVS camera display caused by memory misalignment.",
    "type": "bugfix",
    "function": "Camera",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 150
  },
  {
    "jira": "IVI8394-44",
    "subject": "Adjusting the ALIGN size resolves the issue of certain camera resolutions.",
    "type": "bugfix",
    "function": "Camera",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 151
  },
  {
    "jira": "IVI8394-44",
    "subject": "camera2 hal and EVS HAL add multi-platform compatibility.",
    "type": "feature",
    "function": "Camera",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 152
  },
  {
    "jira": "IVI8394-44",
    "subject": "fix evs can not work on ES5",
    "type": "feature",
    "function": "",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 153
  },
  {
    "jira": "IVI8394-44",
    "subject": "Enumerate all EVS camera IDs regardless of connection status.",
    "type": "feature",
    "function": "",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 154
  },
  {
    "jira": "IVI8397-2049",
    "subject": "Added hot-plugging functionality to the Camera2 interface.",
    "type": "Feature",
    "function": "Camera",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 155
  },
  {
    "jira": "IVI8394-44",
    "subject": "Reduce the log level of the camera HAL that is frequently printed.",
    "type": "feature",
    "function": "",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 156
  },
  {
    "jira": "IVI8394-44",
    "subject": "Check and update camera information when opening the camera.",
    "type": "feature",
    "function": "",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 157
  },
  {
    "jira": "IVI8394-44",
    "subject": "Keep the camera ID and port consistent",
    "type": "feature",
    "function": "",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 158
  },
  {
    "jira": "IVI8394-44",
    "subject": "change the json for camera2",
    "type": "feature",
    "function": "",
    "repo": "proprietary/qcx",
    "owner": "xuefengrui",
    "in_str": False,
    "id": 159
  },
  {
    "jira": "IVI8397-123",
    "subject": "NFS功能 |enable nfs in android",
    "type": "feature",
    "function": "",
    "repo": "kernel/common",
    "owner": "yitianye",
    "in_str": False,
    "id": 164
  },
  {
    "jira": "IVI8397-2541",
    "subject": "Add touch to svm.service",
    "type": "Feature",
    "function": "touch",
    "repo": "crosvm-gunyah",
    "owner": "chengzhou",
    "in_str": False,
    "id": 165
  },
  {
    "jira": "IVI8397-2541",
    "subject": "touch adapt v2.1.2 libgpiod",
    "type": "Feature",
    "function": "touch",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 166
  },
  {
    "jira": "IVI8397-2531",
    "subject": "Modify factory_reset for erase la_misc partition",
    "type": "feature",
    "function": "console",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 167
  },
  {
    "jira": "IVI8397-57",
    "subject": "合入V0.0.08蓝牙和副蓝牙协议栈",
    "type": "features",
    "function": "",
    "repo": "vendor/quectel",
    "owner": "guijunzhou",
    "in_str": False,
    "id": 168
  },
  {
    "jira": "IVI8397-57",
    "subject": "合入主蓝牙和副蓝牙协议栈",
    "type": "features",
    "function": "",
    "repo": "qcom/gen5_gvm",
    "owner": "guijunzhou",
    "in_str": False,
    "id": 169
  },
  {
    "jira": "IVI8397-57",
    "subject": "配置profile属性值",
    "type": "features",
    "function": "",
    "repo": "bt-commonsys-intf",
    "owner": "guijunzhou",
    "in_str": False,
    "id": 170
  },
  {
    "jira": "IVI8397-1096",
    "subject": "移远协议栈新基线移植",
    "type": "features",
    "function": "",
    "repo": "qcom/qssi_au_64",
    "owner": "guijunzhou",
    "in_str": False,
    "id": 171
  },
  {
    "jira": "IVI8397-1096",
    "subject": "移远协议栈新基线移植",
    "type": "features",
    "function": "",
    "repo": "modules/Bluetooth",
    "owner": "guijunzhou",
    "in_str": False,
    "id": 172
  },
  {
    "jira": "IVI8397-2541",
    "subject": "audio adapt v2.1.2 libgpiod",
    "type": "Feature",
    "function": "audio",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 190
  },
  {
    "jira": "IVI8397-2541",
    "subject": "audio adapt v2.1.2 libgpiod",
    "type": "Feature",
    "function": "audio",
    "repo": "voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 191
  },
  {
    "jira": "IVI8397-2541",
    "subject": "display adapt v2.1.2 libgpiod",
    "type": "Feature",
    "function": "display",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 192
  },
  {
    "jira": "IVI8397-2531",
    "subject": "PREFERRED_VERSION_libgpiod = \"1.6.4\"",
    "type": "feature",
    "function": "console",
    "repo": "meta-qti-automotive",
    "owner": "chengzhou",
    "in_str": False,
    "id": 196
  },
  {
    "jira": "IVI8397-135",
    "subject": "Add config of rtl9071 application.",
    "type": "feature",
    "function": "wired-network",
    "repo": "meta-voyah-bsp",
    "owner": "wangyang1",
    "in_str": False,
    "id": 197
  },
  {
    "jira": "IVI8397-126",
    "subject": "IMU driver tree, adapting chip-V1.",
    "type": "Feature",
    "function": "imu-driver",
    "repo": "qcom-opensource/devicetree",
    "owner": "wangyang1",
    "in_str": False,
    "id": 198
  },
  {
    "jira": "IVI8397-129",
    "subject": "Add support for NTFS file system",
    "type": "feature",
    "function": "USB",
    "repo": "kernel/common",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 199
  },
  {
    "jira": "IVI8397-129",
    "subject": "Add automatic mounting for NTFS-formatted USB drives",
    "type": "feature",
    "function": "USB",
    "repo": "qcom/sepolicy_vndr",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 200
  },
  {
    "jira": "IVI8397-129",
    "subject": "Add automatic mounting for NTFS-formatted USB drives",
    "type": "feature",
    "function": "USB",
    "repo": "system/vold",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 201
  },
  {
    "jira": "IVI8397-129",
    "subject": "Add ntfs and exfat format support for linux systems",
    "type": "feature",
    "function": "USB",
    "repo": "kernel/qcom",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 202
  },
  {
    "jira": "IVI8397-129",
    "subject": "Add USB HID whitelist functionality(1/3)",
    "type": "feature",
    "function": "USB",
    "repo": "kernel/common",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 203
  },
  {
    "jira": "IVI8397-129",
    "subject": "Add USB HID whitelist functionality(2/3)",
    "type": "feature",
    "function": "USB",
    "repo": "qcom/common",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 204
  },
  {
    "jira": "IVI8397-129",
    "subject": "Add USB HID whitelist functionality(3/3)",
    "type": "feature",
    "function": "USB",
    "repo": "qcom/sepolicy_vndr",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 205
  },
  {
    "jira": "IVI8397-108",
    "subject": "WiFi BDF Update",
    "type": "feature",
    "function": "WLAN",
    "repo": "test_device",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 206
  },
  {
    "jira": "IVI8397-108",
    "subject": "enable wifi recovery",
    "type": "feature",
    "function": "WLAN",
    "repo": "wlan/platform",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 207
  },
  {
    "jira": "IVI8397-108",
    "subject": "WiFi Debug Tool",
    "type": "feature",
    "function": "WLAN",
    "repo": "wlan/qcacld-3.0",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 208
  },
  {
    "jira": "IVI8397-108",
    "subject": "WiFi Debug Tool",
    "type": "feature",
    "function": "WLAN",
    "repo": "proprietary/wlan",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 209
  },
  {
    "jira": "IVI8397-108",
    "subject": "WiFi Debug Tool",
    "type": "feature",
    "function": "WLAN",
    "repo": "wlan/qca-wifi-host-cmn",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 210
  },
  {
    "jira": "IVI8397-111",
    "subject": "Fix GPIO conflicts with Bluetooth",
    "type": "feature",
    "function": "uart",
    "repo": "vendor/proprietary",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 211
  },
  {
    "jira": "IVI8397-111",
    "subject": "BT Power Control",
    "type": "feature",
    "function": "uart",
    "repo": "qcom-opensource/bt-kernel",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 212
  },
  {
    "jira": "IVI8397-108",
    "subject": "GearVM source code update",
    "type": "feature",
    "function": "WLAN",
    "repo": "amss_standard_oem",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 213
  },
  {
    "jira": "IVI8397-111",
    "subject": "WiFi/BT device tree update",
    "type": "feature",
    "function": "uart",
    "repo": "qcom-opensource/devicetree",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 214
  },
  {
    "jira": "IVI8397-126",
    "subject": "add kernel config of IMU driver in common-kernel.",
    "type": "Feature",
    "function": "imu-driver",
    "repo": "kernel/common",
    "owner": "wangyang1",
    "in_str": False,
    "id": 215
  },
  {
    "jira": "IVI8397-126",
    "subject": "IMU driver IAM-20680,original source code.",
    "type": "Feature",
    "function": "imu-driver",
    "repo": "kernel/common",
    "owner": "wangyang1",
    "in_str": False,
    "id": 217
  },
  {
    "jira": "IVI8397-108",
    "subject": "GearVM bin file update",
    "type": "feature",
    "function": "WLAN",
    "repo": "test_device",
    "owner": "xuejihuang",
    "in_str": False,
    "id": 189
  },
  {
    "jira": "IVI8397-42",
    "subject": "add voyah partition|mount point in init.rc",
    "type": "feature",
    "function": "",
    "repo": "qcom/common",
    "owner": "yitianye",
    "in_str": False,
    "id": 229
  },
  {
    "jira": "IVI8397-168",
    "subject": "gearvm dts/conf, modify uart16 mode and modify TrustZone limit.",
    "type": "feature",
    "function": "gearvm",
    "repo": "amss_standard_oem",
    "owner": "wangyang1",
    "in_str": False,
    "id": 222
  },
  {
    "jira": "IVI8397-168",
    "subject": "add base device-tree of gvm .",
    "type": "feature",
    "function": "baese-drivers",
    "repo": "qcom-opensource/devicetree",
    "owner": "wangyang1",
    "in_str": False,
    "id": 226
  },
  {
    "jira": "IVI8397-2034",
    "subject": "Add rule of merge dtb by oem-id",
    "type": "Feature",
    "function": "GVM",
    "repo": "kernel/build",
    "owner": "mingkunye",
    "in_str": False,
    "id": 235
  },
  {
    "jira": "IVI8397-2034",
    "subject": "Add voyah platform gvm dtbs",
    "type": "Feature",
    "function": "GVM",
    "repo": "qcom-opensource/devicetree",
    "owner": "mingkunye",
    "in_str": False,
    "id": 236
  },
  {
    "jira": "IVI8397-2034",
    "subject": "Add voyah platform pvm dtb",
    "type": "Feature",
    "function": "PVM",
    "repo": "meta-voyah-bsp",
    "owner": "mingkunye",
    "in_str": False,
    "id": 237
  },
  {
    "jira": "IVI8397-2034",
    "subject": "Add voyah platform pvm dtb",
    "type": "Feature",
    "function": "PVM",
    "repo": "vendor/proprietary",
    "owner": "mingkunye",
    "in_str": False,
    "id": 238
  },
  {
    "jira": "IVI8397-2034",
    "subject": "Add voyah platform pvm dtb",
    "type": "Feature",
    "function": "PVM",
    "repo": "base-devicetree",
    "owner": "mingkunye",
    "in_str": False,
    "id": 239
  },
  {
    "jira": "IVI8397-2531",
    "subject": "fix baseline build",
    "type": "feature",
    "function": "baseline",
    "repo": "meta-voyah-bsp",
    "owner": "mingkunye",
    "in_str": False,
    "id": 240
  },
  {
    "jira": "IVI8397-2531",
    "subject": "fix baseline build",
    "type": "feature",
    "function": "baseline",
    "repo": "meta-voyah-bsp",
    "owner": "chengzhou",
    "in_str": False,
    "id": 241
  },
  {
    "jira": "IVI8397-68",
    "subject": "adapt 0128 baseline for voyah",
    "type": "feature",
    "function": "build",
    "repo": "test_device",
    "owner": "chengzhou",
    "in_str": False,
    "id": 242
  },
  {
    "jira": "IVI8397-2034",
    "subject": "delete voyah dtbs for origin baseline",
    "type": "Feature",
    "function": "PVM",
    "repo": "meta-voyah-bsp",
    "owner": "mingkunye",
    "in_str": False,
    "id": 243
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR",
    "type": "bugfix",
    "function": "STR",
    "repo": "external/crosvm",
    "owner": "chengzhou",
    "in_str": True,
    "id": 80
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR",
    "type": "bugfix",
    "function": "STR",
    "repo": "external/crosvm",
    "owner": "chengzhou",
    "in_str": True,
    "id": 82
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR",
    "type": "bugfix",
    "function": "STR",
    "repo": "meta-qti-auto-kernel",
    "owner": "xuejihuang",
    "in_str": True,
    "id": 84
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR",
    "type": "bugfix",
    "function": "STR",
    "repo": "base-devicetree",
    "owner": "xuejihuang",
    "in_str": True,
    "id": 86
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR",
    "type": "bugfix",
    "function": "STR",
    "repo": "test_device",
    "owner": "xuejihuang",
    "in_str": True,
    "id": 88
  },
  {
    "jira": "IVI8397-2546",
    "subject": "Fix issues in STR",
    "type": "bugfix",
    "function": "STR",
    "repo": "amss_standard_oem",
    "owner": "xuejihuang",
    "in_str": True,
    "id": 92
  },
  {
    "jira": "IVI8397-117",
    "subject": "qcom patch for lrms connect fail",
    "type": "Feature",
    "function": "Audio",
    "repo": "test_device",
    "owner": "wenjuanli",
    "in_str": True,
    "id": 104
  },
  {
    "jira": "IVI8397-117",
    "subject": "qcom patch for lrms connect fail",
    "type": "Feature",
    "function": "Audio",
    "repo": "amss_standard_oem",
    "owner": "wenjuanli",
    "in_str": True,
    "id": 105
  },
  {
    "jira": "IVI8397-2642",
    "subject": "resolve cci init fail",
    "type": "Bugfix",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "yupan1",
    "in_str": True,
    "id": 122
  },
  {
    "jira": "IVI8397-168",
    "subject": "fix VFIOInit failed",
    "type": "Bugfix",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "jiashuhou",
    "in_str": True,
    "id": 123
  },
  {
    "jira": "IVI8397-117",
    "subject": "add audio awj",
    "type": "Feature",
    "function": "Audio",
    "repo": "vendor/proprietary",
    "owner": "wenjuanli",
    "in_str": True,
    "id": 136
  },
  {
    "jira": "IVI8397-2642",
    "subject": "bringup driver",
    "type": "Bugfix",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "yupan1",
    "in_str": True,
    "id": 137
  },
  {
    "jira": "IVI8397-2047",
    "subject": "port camera driver",
    "type": "feature",
    "function": "camera",
    "repo": "vendor/proprietary",
    "owner": "jiashuhou",
    "in_str": True,
    "id": 138
  },
  {
    "jira": "IVI8397-2540",
    "subject": "[qcom patch] Fix gvm cpu config",
    "type": "Bug",
    "function": "GVM",
    "repo": "qcom-opensource/devicetree",
    "owner": "mingkunye",
    "in_str": True,
    "id": 144
  },
  {
    "jira": "IVI8397-2540",
    "subject": "[qcom patch] Fix cpu_offline.sh: Exec format error",
    "type": "Feature",
    "function": "PVM",
    "repo": "meta-qti-automotive",
    "owner": "mingkunye",
    "in_str": True,
    "id": 161
  },
  {
    "jira": "IVI8397-123",
    "subject": "NFS功能 |NFS功能selinux执行权限te",
    "type": "feature",
    "function": "",
    "repo": "qcom/sepolicy_vndr",
    "owner": "yitianye",
    "in_str": True,
    "id": 162
  },
  {
    "jira": "IVI8397-123",
    "subject": "NFS功能 |android侧自动挂载",
    "type": "feature",
    "function": "",
    "repo": "qcom/common",
    "owner": "yitianye",
    "in_str": True,
    "id": 163
  },
  {
    "jira": "IVI8397-168",
    "subject": "enable i2c/spi/fs-gpio configuration of gvm common_kernel.",
    "type": "feature",
    "function": "baese-drivers",
    "repo": "kernel/common",
    "owner": "wangyang1",
    "in_str": True,
    "id": 216
  },
  {
    "jira": "IVI8397-168",
    "subject": "enable i2c-qcom-geni-msm configuration of gvm soc-repo.",
    "type": "feature",
    "function": "baese-drivers",
    "repo": "kernel/qcom",
    "owner": "wangyang1",
    "in_str": True,
    "id": 218
  },
  {
    "jira": "IVI8397-42",
    "subject": "add voyah partition|fix superab",
    "type": "feature",
    "function": "",
    "repo": "test_device",
    "owner": "yitianye",
    "in_str": True,
    "id": 219
  },
  {
    "jira": "IVI8397-168",
    "subject": "update gearvm.mbn, fix Trustzone error..",
    "type": "feature",
    "function": "gearvm",
    "repo": "test_device",
    "owner": "wangyang1",
    "in_str": True,
    "id": 220
  },
  {
    "jira": "IVI8397-168",
    "subject": "devcfg TZ binary file.",
    "type": "feature",
    "function": "baese-drivers",
    "repo": "test_device",
    "owner": "wangyang1",
    "in_str": True,
    "id": 221
  },
  {
    "jira": "IVI8397-168",
    "subject": "modify file vhost-user-scmi.service.",
    "type": "feature",
    "function": "scmi-config",
    "repo": "vhost-user-scmi",
    "owner": "wangyang1",
    "in_str": True,
    "id": 223
  },
  {
    "jira": "IVI8397-168",
    "subject": "add base device-tree of pvm kernel.",
    "type": "feature",
    "function": "baese-drivers",
    "repo": "base-devicetree",
    "owner": "wangyang1",
    "in_str": True,
    "id": 224
  },
  {
    "jira": "IVI8397-168",
    "subject": "tz configuration, resource assign and QUP assign.",
    "type": "feature",
    "function": "trustzone",
    "repo": "test_device",
    "owner": "wangyang1",
    "in_str": True,
    "id": 225
  },
  {
    "jira": "IVI8397-2194",
    "subject": "memory_dump_v21.ko 编译带上with debug_info",
    "type": "Feature",
    "function": "log",
    "repo": "meta-voyah-bsp",
    "owner": "yitianye",
    "in_str": True,
    "id": 227
  },
  {
    "jira": "IVI8397-42",
    "subject": "modify superimg to 30G|gen5_gvm",
    "type": "feature",
    "function": "",
    "repo": "qcom/gen5_gvm",
    "owner": "yitianye",
    "in_str": True,
    "id": 228
  },
  {
    "jira": "IVI8397-123",
    "subject": "NFS功能 |fix nfs-server can't alloc mem",
    "type": "feature",
    "function": "",
    "repo": "kernel/qcom",
    "owner": "yitianye",
    "in_str": True,
    "id": 230
  },
  {
    "jira": "IVI8397-88",
    "subject": "add recoveryinfo in cmdline|abl part.",
    "type": "Feature",
    "function": "",
    "repo": "tianocore/edk2",
    "owner": "yitianye",
    "in_str": True,
    "id": 231
  },
  {
    "jira": "IVI8397-42",
    "subject": "add voyah partition",
    "type": "feature",
    "function": "",
    "repo": "test_device",
    "owner": "yitianye",
    "in_str": True,
    "id": 232
  },
  {
    "jira": "IVI8397-23",
    "subject": "fix fastboot can not trgger by debug uart",
    "type": "Bug",
    "function": "",
    "repo": "test_device",
    "owner": "mingkunye",
    "in_str": True,
    "id": 233
  },
  {
    "jira": "IVI8397-2034",
    "subject": "read ADC to judge hardware version and match dtb by oem-id",
    "type": "Feature",
    "function": "PVM/GVM",
    "repo": "test_device",
    "owner": "mingkunye",
    "in_str": True,
    "id": 234
  },
  {
    "jira": "IVI8397-2540",
    "subject": "voyahpm-bsp adapt v2.1.2 libgpiod",
    "type": "Feature",
    "function": "PowerManager",
    "repo": "voyah-bsp",
    "owner": "mingkunye",
    "in_str": True,
    "id": 193
  },
  {
    "jira": "IVI8397-2540",
    "subject": "voyahpm-bsp adapt v2.1.2 libgpiod",
    "type": "Feature",
    "function": "PowerManager",
    "repo": "meta-voyah-bsp",
    "owner": "mingkunye",
    "in_str": True,
    "id": 194
  },
  {
    "jira": "IVI8397-31",
    "subject": "Init packaging scripts from bsp_rc16_6.2_20260128.",
    "type": "Feature",
    "function": "",
    "repo": "test_device",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 160
  },
  {
    "jira": "IVI8397-31",
    "subject": "Remove the updater tool from built_ota_tools.",
    "type": "Feature",
    "function": "",
    "repo": "platform/build_repo",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 173
  },
  {
    "jira": "IVI8397-31",
    "subject": "Adapting init to Android single partition",
    "type": "Feature",
    "function": "",
    "repo": "qcom-opensource/kiumd",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 174
  },
  {
    "jira": "IVI8397-31",
    "subject": "Link la_super_a and la_super_b to la_super.",
    "type": "Feature",
    "function": "",
    "repo": "qcom-opensource/kiumd",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 175
  },
  {
    "jira": "IVI8397-31",
    "subject": "Adapting init to Android single partition",
    "type": "Feature",
    "function": "",
    "repo": "crosvm-gunyah",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 176
  },
  {
    "jira": "IVI8397-31",
    "subject": "Adapting init to Android single partition.",
    "type": "Feature",
    "function": "",
    "repo": "system/core",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 177
  },
  {
    "jira": "IVI8397-31",
    "subject": "Adapting init to Android single partition",
    "type": "Feature",
    "function": "",
    "repo": "system/core",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 178
  },
  {
    "jira": "IVI8397-31",
    "subject": "Adapting nonab fstab to Android single partition.",
    "type": "Feature",
    "function": "",
    "repo": "qcom/gen5_gvm",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 179
  },
  {
    "jira": "IVI8397-31",
    "subject": "Adapting init ab_suffix to android single partition.",
    "type": "Feature",
    "function": "",
    "repo": "system/core",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 180
  },
  {
    "jira": "IVI8397-31",
    "subject": "Add the la_super_b partition.",
    "type": "Feature",
    "function": "",
    "repo": "test_device",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 181
  },
  {
    "jira": "IVI8397-42",
    "subject": "add voyah partition |gvm dtsi",
    "type": "feature",
    "function": "",
    "repo": "qcom-opensource/devicetree",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 182
  },
  {
    "jira": "IVI8397-31",
    "subject": "Adapt the Android build for single partition image packaging.",
    "type": "Feature",
    "function": "",
    "repo": "qcom/vendor-common",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 183
  },
  {
    "jira": "IVI8397-31",
    "subject": "Add gen5_gvm and himalayas to NON_AB_TARGET_LIST.",
    "type": "Feature",
    "function": "",
    "repo": "qcom-opensource/core-utils",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 184
  },
  {
    "jira": "IVI8397-31",
    "subject": "Adapt for Android single partition, set ENABLE_AB to false.",
    "type": "Feature",
    "function": "",
    "repo": "qcom/gen5_gvm",
    "owner": "xuefengrui",
    "in_str": True,
    "id": 185
  },
  {
    "jira": "IVI8397-42",
    "subject": "add voyah partition |gvm dtsi",
    "type": "feature",
    "function": "",
    "repo": "qcom-opensource/devicetree",
    "owner": "yitianye",
    "in_str": True,
    "id": 186
  },
  {
    "jira": "IVI8397-42",
    "subject": "add voyah partition |pvm dtsi",
    "type": "feature",
    "function": "",
    "repo": "base-devicetree",
    "owner": "yitianye",
    "in_str": True,
    "id": 187
  },
  {
    "jira": "IVI8397-42",
    "subject": "add voyah partition |8797server",
    "type": "feature",
    "function": "",
    "repo": "crosvm-gunyah",
    "owner": "yitianye",
    "in_str": True,
    "id": 188
  }
]
