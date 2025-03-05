# ##### BEGIN GPL LICENSE BLOCK #####
#
#    GNU GPLv3, 29 June 2007
#
#    Examples from Ch8 of the book "Blender Scripting with Python" by Isabel Lupiani.
#    Copyright (C) 2024  Isabel Lupiani, Apress.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from mathutils import Euler
from math import radians

from view_fit import get_context_override

def load_image_empty(context, name, image_file_path, location, rotation_degrees, depth, side, transparency):
    empty = bpy.data.objects.new(name, None)
    empty.empty_display_type = 'IMAGE'
    empty.data = bpy.data.images.load(image_file_path)    
    empty.location = location
    empty.rotation_euler = Euler((radians(d) for d in rotation_degrees), 'XYZ')
    empty.empty_image_depth = depth
    empty.empty_image_side = side
    empty.color[3] = transparency
    empty.empty_display_size = 5
    context.collection.objects.link(empty)

def rename_empty(context, name):
    active_obj = context.view_layer.objects.active
    if active_obj and active_obj.type == 'EMPTY':
        active_obj.name = name
    else:
        num_objs = len(context.view_layer.objects)
        for i in range(num_objs - 1, -1, -1):
            obj = context.view_layer.objects[i]
            if obj.type == 'EMPTY':
                obj.name = name
                context.view_layer.objects.active = obj
                break

def load_reference_or_background_image(context, filepath, name, location, rotation_degrees=(90,0,0), is_background=False):
    rotation_rads = [radians(d) for d in rotation_degrees]
    context_override = get_context_override(context, 'VIEW_3D', 'WINDOW')
    with bpy.context.temp_override(**context_override):  
        bpy.ops.object.empty_image_add(filepath=filepath, relative_path=False, align='VIEW', \
            location=location, rotation=rotation_rads, scale=(1,1,1), background=is_background)
        rename_empty(context, name)
        