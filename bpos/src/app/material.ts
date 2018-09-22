import { MatButtonModule, MatToolbarModule, MatCheckboxModule, MatIconModule } from '@angular/material';
import { NgModule } from '@angular/core';
import {MatMenuModule} from '@angular/material/menu';

@NgModule({
    imports: [MatButtonModule, MatToolbarModule, MatCheckboxModule, MatIconModule, MatMenuModule],
    exports: [MatButtonModule, MatToolbarModule, MatCheckboxModule, MatIconModule, MatMenuModule],
})
export class MaterialModule {}
