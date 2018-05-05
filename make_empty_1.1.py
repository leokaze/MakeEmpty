bl_info = {
    "name": "Make Empty",
    "author": "Leonardo Cáceres",
    "version": (1, 1),
    "blender": (2, 70, 0),
    "location": "Tools > Make Empty > ",
    "description": "Adds a new Mesh Object",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Tools"}

import bpy

def MakeEmpty(ob):
    if ob.type == 'MESH':
        ob.draw_type = 'WIRE'
        ob.hide_render = True
        ob.show_all_edges = True

def MakeSolid(ob):
    if ob.type == 'MESH':
        ob.draw_type = 'SOLID'
        ob.hide_render = False
        ob.show_all_edges = False


class MakeEmptyOperator(bpy.types.Operator):
    """Make selected object an empty object"""
    bl_idname = "make.empty_operator"
    bl_label = "Make Empty Operator"
    bl_options = {'UNDO'}

    makeES= bpy.props.BoolProperty()

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        for o in context.selected_objects:
            if self.makeES:
                MakeEmpty(o)
            else:
                MakeSolid(o)
        return {'FINISHED'}
    

class MakeEmptyPanel(bpy.types.Panel):
    """Panel Principal"""
    bl_idname = "VIEW3D_PT_make_empty"
    bl_label = "Make Empty"
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = 'Tools'
    bl_context = "objectmode"
    
    
    def draw(self, context):
        layout = self.layout
        layout.operator(MakeEmptyOperator.bl_idname, text = "Make Empty").makeES = True
        layout.operator(MakeEmptyOperator.bl_idname, text = "Make Solid").makeES = False

def register():
    bpy.utils.register_class(MakeEmptyOperator)
    bpy.utils.register_class(MakeEmptyPanel)

def unregister():
    bpy.utils.unregister_class(MakeEmptyOperator)
    bpy.utils.unregister_class(MakeEmptyPanel)
    
if __name__ == "__main__":
    register()
