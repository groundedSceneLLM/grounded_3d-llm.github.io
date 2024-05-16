import numpy as np
from plyfile import PlyData, PlyElement

def change_vertex_colors_to_yellow(ply_files):
    # yellow_color = np.array([255, 153, 51], dtype=np.uint8)  # RGB for yellow

    for file_path in ply_files:
        # Read the PLY file
        ply_data = PlyData.read(file_path)
        vertices = ply_data['vertex'].data

        # Create a new structured numpy array with the same dtype as the original
        # new_vertex_data = np.empty(vertices.shape, dtype=vertices.dtype)
        
        # # Copy the original data
        # for name in vertices.dtype.names:
        #     # if name in ['red', 'green', 'blue']:
        #     #     continue
        #     new_vertex_data[name] = vertices[name]
        
        # # Update colors to yellow
        # # new_vertex_data['red'] = yellow_color[0]
        # # new_vertex_data['green'] = yellow_color[1]
        # # new_vertex_data['blue'] = yellow_color[2]

        # # Create a new PlyElement for saving to file
        total_vertices = len(vertices)
        sampled_indices = np.random.choice(total_vertices, total_vertices // 2, replace=False)
        sampled_vertices = vertices[sampled_indices]

        new_vertex_element = PlyElement.describe(sampled_vertices, 'vertex')

        # Save the modified PLY file
        modified_file_path = file_path
        PlyData([new_vertex_element], obj_info="").write(modified_file_path)
        print(f"Modified file saved as: {modified_file_path}")


# Example usage
if __name__ == '__main__':
    root = "/instance_raw.ply"
    ply_files = [
        # "assets/scene0011_00"+ root,
        # "assets/scene0015_00"+ root,
        # "assets/scene0050_00"+ root,
        # "assets/scene0086_00"+ root,
        # "assets/scene0144_00"+ root,
        # "assets/scene0196_00"+ root,
        "assets/scene0426_00"+ root,

    ]
    change_vertex_colors_to_yellow(ply_files)
