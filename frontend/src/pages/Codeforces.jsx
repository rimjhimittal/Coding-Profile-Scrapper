import React from 'react';
import { GridComponent, ColumnsDirective, ColumnDirective, Resize, Sort, ContextMenu, Filter, Page, ExcelExport, PdfExport, Edit, Inject } from '@syncfusion/ej2-react-grids';
import { contextMenuItems, ordersGrid } from '../data/dummy';
import { Header } from '../components';

const output = [];

class Codeforces extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      output,
      // loading: true,
    };
  }

  render() {
    const editing = { allowDeleting: true, allowEditing: true };
    return (
      <div className="m-2 md:m-10 mt-24 p-2 md:p-10 bg-light-gray rounded-3xl">
        <Header category="Codeforces" title="Leaderboard" />
        <GridComponent
          id="gridcomp"
          dataSource={this.state.output}
          allowPaging
          allowSorting
          allowExcelExport
          allowPdfExport
          contextMenuItems={contextMenuItems}
          editSettings={editing}
        >
          {/* let n = 1; */}
          <ColumnsDirective>
            <ColumnDirective field="serialno" headerText="Intra Rank" width="70" />
            <ColumnDirective
              field="photo_url"
              headerText="Profile Photo"
              align="center"
              width="120"
              template={(rowData) => <img src={rowData.photo_url} alt="Profile" width="50" height="50" />}
            />
            <ColumnDirective field="name" headerText="Name" textAlign="center" width="90" />
            <ColumnDirective field="rank" headerText="Rank" textAlign="center" width="120" />
            <ColumnDirective field="number_of_questions" headerText="Number of Questions" textAlign="center" width="120" />
            <ColumnDirective field="last_solved" headerText="Last Solved" textAlign="center" width="120" />
            <ColumnDirective field="username" headerText="Username" textAlign="center" width="120" />

          </ColumnsDirective>
          <Inject services={[Resize, Sort, ContextMenu, Filter, Page, ExcelExport, Edit, PdfExport]} />
        </GridComponent>
      </div>
    );
  }
}

export default Codeforces;
