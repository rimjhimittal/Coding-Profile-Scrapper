import axios from 'axios';
import React from 'react';
import { GridComponent, ColumnsDirective, ColumnDirective, Resize, Sort, ContextMenu, Filter, Page, ExcelExport, PdfExport, Edit, Inject } from '@syncfusion/ej2-react-grids';
import { contextMenuItems, ordersGrid } from '../data/dummy';
import { Header } from '../components';


const url = 'http://127.0.0.1:8000/getCodechefInfo/'

export default function Codechef ()  {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    axios.get(url).then((response) => {
      setPost(response.data);
    });
  }, []);
  console.log(post);
  if (!post) return null;
  const editing = { allowDeleting: true, allowEditing: true };

  return (
    <div className="m-2 md:m-10 mt-24 p-2 md:p-10 bg-white rounded-3xl">
      <Header category="Codechef" title="Leaderboard" />
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
            <ColumnDirective field="rating" headerText="Rating" textAlign="center" width="120" />
            <ColumnDirective field="global_rank" headerText="Global Rank" textAlign="center" width="120" />
            <ColumnDirective field="country_rank" headerText="Country Rank" textAlign="center" width="120" />
            <ColumnDirective field="stars" headerText="Stars" textAlign="center" width="120" />
            <ColumnDirective field="number_of_questions" headerText="Number of Questions" textAlign="center" width="120" />
            

          </ColumnsDirective>
          <Inject services={[Resize, Sort, ContextMenu, Filter, Page, ExcelExport, Edit, PdfExport]} />

      </GridComponent>
    </div>
  );
};

