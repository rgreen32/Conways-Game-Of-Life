use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyclass(unsendable)]
struct Cell{
    position_x: usize,
    position_y: usize,
    rect_x: i32,
    rect_y: i32,
    #[pyo3(get, set)]
    canvas_id: i32,
    was_alive: bool,
    #[pyo3(get)]
    is_alive: bool
}
#[pymethods]
impl Cell {
    #[new]
    fn new(position_x: usize, position_y: usize, rect_x: i32, rect_y: i32) -> Self {
        Cell { position_x, position_y, rect_x, rect_y, canvas_id: 0, was_alive: false, is_alive: false }
    }

    #[getter(canvas_id)]
    fn canvas_id(&self) -> PyResult<i32> {
        Ok(self.canvas_id)
    }

    #[setter(canvas_id)]
    fn set_canvas_id(&mut self, value: i32) -> PyResult<()> {
        self.canvas_id = value;
        Ok(())
    }
}

#[pyclass(unsendable)]
struct Grid{
    pub cells: Vec<Vec<Cell>>,
    window_height: i32,
    window_width: i32,
    pixel_ratio: usize
}
#[pymethods]
impl Grid {
    #[new]
    fn new(window_height: i32, window_width: i32, number_of_cells_y_axis: i32) -> Self {
        let pixel_ratio = (window_height/number_of_cells_y_axis) as usize;
        let mut cell_rows: Vec<Vec<Cell>> = Vec::new();
        for (row_index, rect_x) in (0..window_width).step_by(pixel_ratio).enumerate(){
            let mut cell_column: Vec<Cell> = Vec::new();
            for (column_index, rect_y) in (0..window_height).step_by(pixel_ratio).enumerate(){
                let cell = Cell{position_x: row_index, position_y: column_index, rect_x, rect_y, canvas_id: 0, was_alive: false, is_alive: false};
                cell_column.push(cell);
            }
            cell_rows.push(cell_column);
        }
        // let number_of_cells_y_axis = ((self.canvas_height)/(self.canvas_pixels_to_meters_ratio as f32*self.cell_side_length_meters as f32)) as usize;
        Grid { window_height, window_width, pixel_ratio, cells: cell_rows}
    }

    #[getter(cells)]
    fn cells(&self) -> PyResult<Vec<Vec<Cell>>> {
        Ok(self.canvas_id)
    }

    #[setter(canvas_id)]
    fn set_canvas_id(&mut self, value: i32) -> PyResult<()> {
        self.canvas_id = value;
        Ok(())
    }
}


#[pymodule]
/// A Python module implemented in Rust.
fn grid(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Cell>()?;
    m.add_class::<Grid>()?;
    Ok(())
}