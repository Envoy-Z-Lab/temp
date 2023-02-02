# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
# Copyright (C) 2017-2020 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

def FullOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def IncrementalOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def AddImage(info, basename, dest):
  name = basename
  path = "IMAGES/" + name
  if path not in info.input_zip.namelist():
    return

  data = info.input_zip.read(path)
  common.ZipWriteStr(info.output_zip, name, data)
  info.script.Print("Patching {} image unconditionally...".format(dest.split('/')[-1]))
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (name, dest))

def OTA_InstallEnd(info):
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/anr");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/backup/pending");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/cache");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/crashdata");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/last_alog");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/last_kmsg");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/local");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/log");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/mlog ");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/resource-cache");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system/appusagestates");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system/dropbox");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system/graphicsstats");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system/netstats");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system/package_cache");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system/procstats");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system/shared_prefs");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system/syncmanager-log");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system/usagestats");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system_ce/0/recent_images");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system_ce/0/recent_tasks");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system_ce/0/snapshots");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/system_ce/0/usagestats");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/tmp");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/tombstones");')
  info.script.AppendExtra('run_program("/system/bin/rm", "-rf", "/data/vendor/wlan_logs");')
  return
