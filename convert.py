import open3d as o3d

print("Testing IO for point cloud ...")
pcd = o3d.io.read_point_cloud("assets/seg_with_origin.ply")
print(pcd)
o3d.io.write_triangle_mesh("assets/seg_with_origin.glb", pcd)
