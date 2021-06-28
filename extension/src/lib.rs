use pyo3::prelude::*;
use pyo3::types::PyList;
use pyo3::types::PyTuple;

#[pyclass(unsendable)]
struct Cell{
    position_x: i32,
    position_y: i32,
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
    fn new(position_x: i32, position_y: i32, rect_x: i32, rect_y: i32) -> Self {
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

fn get_live_neighbors(cells: &Vec<Vec<Cell>>, cell: &Cell) -> usize{
    let mut live_neighbors = 0;

    let cell_map_x_length = (cells.len()-1) as i32;
    let cell_map_y_length = (cells[0].len()-1) as i32;
    for position_x in (cell.position_x-1..cell.position_x+2){

        if (position_x < 0 || position_x > cell_map_x_length){continue}

        for position_y in (cell.position_y-1..cell.position_y+2){
            if (position_y < 0 || position_y > cell_map_y_length){continue}
            else if (position_x == cell.position_x && position_y == cell.position_y){continue}

            let neighboring_cell = &cells[position_x as usize][position_y as usize];
            if (neighboring_cell.was_alive){
                live_neighbors += 1
            }
        }
    }

    return live_neighbors
}

fn cell_is_alive(cells: &Vec<Vec<Cell>>, cell: &Cell) -> bool{
    let live_neighbors = get_live_neighbors(&cells, &cell);

    if (cell.was_alive && (live_neighbors == 2 || live_neighbors == 3)){
        return true
    }else if (!cell.was_alive && live_neighbors ==3) {
        return true
    }else{
        return false
    }
    
}


#[pyclass(unsendable)]
struct Grid{
    pub cells: Vec<Vec<Cell>>
}
#[pymethods]
impl Grid {
    #[new]
    fn new(cells: &PyList) -> Self {
        // let pixel_ratio = (window_height/number_of_cells_y_axis) as i32;
        // let gil = Python::acquire_gil();
        // let py = gil.python();
        let cell_rows: Vec<&PyList> = cells.extract().unwrap();
        let mut rust_cell_rows: Vec<Vec<Cell>> = Vec::new();
        for cell_column in cell_rows{
            let mut rust_cell_column: Vec<Cell> = Vec::new();
            let new_cell_column: Vec<&PyTuple> = cell_column.extract().unwrap();
            for cell in new_cell_column{
                let cell_values: (i32, i32, i32, i32, i32, bool, bool) = cell.extract().unwrap();
                let rust_cell = Cell{position_x: cell_values.0, position_y: cell_values.1, rect_x: cell_values.2, rect_y: cell_values.3, canvas_id: cell_values.4, was_alive: cell_values.5, is_alive: cell_values.6};
                rust_cell_column.push(rust_cell)
            }
            rust_cell_rows.push(rust_cell_column)
        }

        Grid {cells: rust_cell_rows}
    }

    fn sim_step(&mut self){
        for cell_column in &mut self.cells{
            for cell in cell_column{
                // let cell_is_alive = cell_is_alive(&self.cells, cell);
                // cell.is_alive = cell_is_alive;
            }
        }
    }





    // #[setter(cells)]
    // fn set_canvas_id(&mut self, position_x: usize, position_y: usize, is_alive: bool) -> PyResult<()> {
    //     self.canvas_id = value;
    //     Ok(())
    // }
}


#[pymodule]
/// A Python module implemented in Rust.
fn grid(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Cell>()?;
    m.add_class::<Grid>()?;
    Ok(())
}