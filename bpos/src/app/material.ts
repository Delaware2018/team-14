import { MatButtonModule, MatToolbarModule, MatCheckboxModule, MatIconModule } from '@angular/material';
import { NgModule } from '@angular/core';

@NgModule({
    imports: [MatButtonModule, MatToolbarModule, MatCheckboxModule, MatIconModule],
    exports: [MatButtonModule, MatToolbarModule, MatCheckboxModule, MatIconModule],
})
export class MaterialModule {}
