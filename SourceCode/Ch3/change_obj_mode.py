# ##### BEGIN GPL LICENSE BLOCK #####
#
#    GNU GPLv3, 29 June 2007
#
#    Example from Ch3 of the book "Blender Scripting with Python" by Isabel Lupiani. 
#    Switch the default Cube object to Edit mode in Python.
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

def change_obj_to_edit_mode(mesh_obj_name: str):
    for obj in bpy.context.scene.objects:
        obj.select_set(False)
        
    if mesh_obj_name and bpy.context.scene.objects.find(mesh_obj_name) >= 0:
        mesh_obj = bpy.context.scene.objects[mesh_obj_name]
        if mesh_obj.type == 'MESH':
            bpy.context.view_layer.objects.active = mesh_obj
            bpy.ops.object.mode_set(mode='EDIT')
            
def change_obj_to_mode(obj_name: str, obj_type, mode_to_set):
    for obj in bpy.context.scene.objects:
        obj.select_set(False)
        
    if obj_name and bpy.context.scene.objects.find(obj_name) >= 0:
        obj = bpy.context.scene.objects[obj_name]
        if obj.type == obj_type:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode=mode_to_set)
        
if __name__ == "__main__":
    change_obj_to_edit_mode('Cube')
    #change_obj_to_mode('Cube', 'MESH', 'EDIT')
