bl_info = {
    "name": "make empty",
    "author": "Leonardo Caceres",
    "version": (1, 0),
    "blender": (2, 79, 0),
    "location": "View3D > Tools > Misc > Make Empty",
    "description": "make an object empty object",
    "warning": "",
    "wiki_url": "",
    "category": "tools",
    }


import bpy


#OPERATOR MAKE EMPTY
class OP_make_empty(bpy.types.Operator):
    """make the selected objetc a empty object"""
    bl_idname = "object.make_empty"
    bl_label = "Make Empty"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        ob = bpy.context.active_object
        bpy.context.object.draw_type = 'WIRE'
        bpy.context.object.hide_render = True
        return {'FINISHED'}
    
#PANEL
class LayoutMakeEmpty(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Make Empty"
    bl_idname = "LAYOUT_make_empty"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        
        col = layout.column(align=True)
        col.operator("object.make_empty")

# Registration
def register():
    bpy.utils.register_class(OP_make_empty)
    bpy.utils.register_class(LayoutMakeEmpty)


def unregister():
    bpy.utils.unregister_class(OP_make_empty)
    bpy.utils.unregister_class(LayoutMakeEmpty)


if __name__ == "__main__":
    register()
