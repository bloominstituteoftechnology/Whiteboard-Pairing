fn zeros_to_the_right(arr: &mut [i32]) -> i32 {
  let mut left: usize = 0;
  let mut right = arr.len() - 1;
  let mut n_non_zeros: i32 = 0;

  while left <= right {
    if arr[left] == 0 && arr[right] != 0 {
      arr.swap(left, right);
      left += 1;
      right -= 1;
      n_non_zeros += 1;
    } else {
      if arr[left] != 0 { 
        left += 1; 
        n_non_zeros += 1;
      } 
      if arr[right] == 0 { 
        if right > 0 { right -= 1; } else { break; }
      }
    }
  }

  n_non_zeros
}

fn main() {
  let mut arr1 = vec![0, 3, 1, 0, -2];
  println!("Number of non-zero integers: {}", zeros_to_the_right(&mut arr1));
  println!("{:?}", arr1);
  // should print:
  // [-2, 3, 1, 0, 0]
  // Number of non-zero integers: 3

  let mut arr2 = vec![1, 2, 3, 0, 4, 0, 0];
  println!("Number of non-zero integers: {}", zeros_to_the_right(&mut arr2));
  println!("{:?}", arr2);
  // should print:
  // [1, 2, 3, 4, 0, 0, 0]
  // Number of non-zero integers: 4

  let mut arr3 = vec![4, 1, 2, 5];
  println!("Number of non-zero integers: {}", zeros_to_the_right(&mut arr3));
  println!("{:?}", arr3);
  // should print:
  // [4, 1, 2, 5]
  // Number of non-zero integers: 4

  let mut arr4 = vec![0, 0, 0, 0, 0];
  println!("Number of non-zero integers: {}", zeros_to_the_right(&mut arr4));
  println!("{:?}", arr4); 
  // should print:
  // [0, 0, 0, 0, 0]
  // Number of non-zero integers: 0

  let mut arr5 = vec![0, 0, 0, 0, 3, 2, 1];
  println!("Number of non-zero integers: {}", zeros_to_the_right(&mut arr5));
  println!("{:?}", arr5);
  // should print:
  // [1, 2, 3, 0, 0, 0, 0]
  // Number of non-zero integers: 3
}