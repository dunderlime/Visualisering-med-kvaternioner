bl_info = {
    "name": "Visualisering av kvaternion Gauss map",
    "author": "Emil Hietanen",
    "version": (1, 0),
    "blender": (2, 80, 0),

}


import bpy

bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0))
    bpy.ops.mesh.bisect(plane_co=(-0.390101, 0.169852, 0.854357), plane_no=(0.407088, 0.913326, -0.0107618), xstart=791, xend=793, ystart=588, yend=45)

bpy.ops.mesh.primitive_uv_sphere_add(location=(0, 0, 0))
  py.ops.mesh.bisect(plane_co=(-0.390101, 0.169852, 0.854357), plane_no=(0.407088, 0.913326, -0.0107618), xstart=791, xend=793, ystart=588, yend=45)
  bpy.context.space_data.overlay.show_ortho_grid = True
  bpy.context.object.rotation_mode = 'QUATERNION'
  bpy.context.object.rotation_quaternion[0] = 0
  bpy.context.object.rotation_quaternion[1] = 1
  bpy.context.object.rotation_quaternion[2] = 0
  bpy.context.object.rotation_quaternion[3] = 0
  
bpy.context.space_data.shading.type = 'SOLID'
bpy.context.space_data.shading.type = 'WIREFRAME'
bpy.context.space_data.shading.type = 'WIREFRAME'
bpy.context.space_data.shading.type = 'WIREFRAME'
bpy.context.space_data.shading.type = 'SOLID'
bpy.context.space_data.shading.type = 'MATERIAL'
bpy.context.space_data.shading.type = 'RENDERED'


return {'FINISHED'}

