import axios from 'axios';
import React from 'react';
import { GridComponent, ColumnsDirective, ColumnDirective, Resize, Sort, ContextMenu, Filter, Page, ExcelExport, PdfExport, Edit, Inject } from '@syncfusion/ej2-react-grids';
import { contextMenuItems, ordersGrid } from '../data/dummy';
import { Header } from '../components';

// const output = [{
//   username: 'rimjhimittal',
//   name: 'Rimjhim Mittal',
//   rank: '900,547',
//   photo_url: 'https://assets.leetcode.com/users/avatars/avatar_1668491883.png',
//   number_of_questions: 58,
//   last_solved: '10 days ago',
// },
// {
//   username: 'rimjhimittal',
//   name: 'Rimjhim Mittal',
//   rank: '900,547',
//   photo_url: 'https://assets.leetcode.com/users/avatars/avatar_1668491883.png',
//   number_of_questions: 58,
//   last_solved: '10 days ago',
// },
// {
//   username: 'rimjhimittal',
//   name: 'Rimjhim Mittal',
//   rank: '900,547',
//   photo_url: 'https://assets.leetcode.com/users/avatars/avatar_1668491883.png',
//   number_of_questions: 58,
//   last_solved: '10 days ago',
// }];

// const output = await axios.get('http://127.0.0.1:8000/getLeetcodeInfo/')

const url = 'http://127.0.0.1:8000/getLeetcodeInfo/'

// let fetchdata = async () => {
//   let output = await axios.get('http://127.0.0.1:8000/getLeetcodeInfo/');
//   return output;
// }

export default function Leetcode() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    axios.get(url).then((response) => {
      setPost(response.data);
    });
  }, []);
  console.log(post);
  if (!post) return null;

  // return (
  //   <div>
  //     <h1>{post.title}</h1>
  //     <p>{post.body}</p>
  //   </div>
  // );
  const editing = { allowDeleting: true, allowEditing: true };
    return (
      <div className="m-2 md:m-10 mt-24 p-2 md:p-10 bg-white rounded-3xl">
        <Header category="Leetcode" title="Leaderboard" />
        <GridComponent
          id="gridcomp"
          dataSource={post}
          allowPaging
          allowSorting
          allowExcelExport
          allowPdfExport
          contextMenuItems={contextMenuItems}
          editSettings={editing}
        >
          {/* let n = 1; */}
          <ColumnsDirective>
            <ColumnDirective field="serialNumber" headerText="Intra Rank" width="70" />
            <ColumnDirective
              field="photo_url"
              headerText="Profile Photo"
              align="center"
              width="120"
              template={(rowData) => <img src={rowData.photo_url} style={{ borderRadius: "50%" }} alt="Profile" width="50" height="50" />}
            />
            <ColumnDirective field="name" headerText="Name" textAlign="center" width="90" />
            <ColumnDirective field="username" headerText="Username" textAlign="center" width="120" />
            <ColumnDirective field="rank" headerText="Rank" textAlign="center" width="120" />
            <ColumnDirective field="number_of_questions" headerText="Number of Questions" textAlign="center" width="120" />
            <ColumnDirective field="last_solved" headerText="Last Solved" textAlign="center" width="120" />

          </ColumnsDirective>
          <Inject services={[Resize, Sort, ContextMenu, Filter, Page, ExcelExport, Edit, PdfExport]} />
        </GridComponent>
      </div>
    );
}

// class Leetcode extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       output,
//       // loading: true,
//     };
//   }

//   render() {
//     const editing = { allowDeleting: true, allowEditing: true };
//     return (
//       <div className="m-2 md:m-10 mt-24 p-2 md:p-10 bg-light rounded-3xl">
//         <Header category="Leetcode" title="Leaderboard" />
//         <GridComponent
//           id="gridcomp"
//           dataSource={this.state.output}
//           allowPaging
//           allowSorting
//           allowExcelExport
//           allowPdfExport
//           contextMenuItems={contextMenuItems}
//           editSettings={editing}
//         >
//           {/* let n = 1; */}
//           <ColumnsDirective>
//             <ColumnDirective field="serialno" headerText="Intra Rank" width="70" />
//             <ColumnDirective
//               field="photo_url"
//               headerText="Profile Photo"
//               align="center"
//               width="120"
//               template={(rowData) => <img src={rowData.photo_url} alt="Profile" width="50" height="50" />}
//             />
//             <ColumnDirective field="name" headerText="Name" textAlign="center" width="90" />
//             <ColumnDirective field="rank" headerText="Rank" textAlign="center" width="120" />
//             <ColumnDirective field="number_of_questions" headerText="Number of Questions" textAlign="center" width="120" />
//             <ColumnDirective field="last_solved" headerText="Last Solved" textAlign="center" width="120" />
//             <ColumnDirective field="username" headerText="Username" textAlign="center" width="120" />

//           </ColumnsDirective>
//           <Inject services={[Resize, Sort, ContextMenu, Filter, Page, ExcelExport, Edit, PdfExport]} />
//         </GridComponent>
//       </div>
//     );
//   }
// }

// export default Leetcode;
